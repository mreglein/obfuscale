# JSD Challenge Score: Algorithm and Labels

This document describes how the JSD-based challenge score is computed for binary obfuscation pairs (Lk vs L0), the default weights and thresholds, and how per-pair labels are assigned (L1/L2/L3).

**Correction (this pass):** this document previously claimed `jsd_vs_L0` is
computed between *byte* histograms. The actual generator
(`recompute_jsd_from_manifest.py`) computes it between **entropy-windowed**
histograms (`jsd_e`); a separate byte-histogram JSD (`jsd_b`) exists but is
not the value used here. Any prior figures computed from this column
describe entropy divergence, not byte divergence.

## Inputs (from `pairwise_jsd_vs_L0.csv`)
For each Lk (k>0) variant strictly paired to its L0 original (rows where `compare` starts with `L0-`):
- `jsd_vs_L0` (float): Jensen–Shannon distance in base 2 between **entropy-windowed** histograms (0..1). See correction above.
- `delta_entropy` (float): entropy(Lk) − entropy(L0) in bits.
- `delta_diffstd` (float): diff-std(Lk) − diff-std(L0); positive suggests more diffusion/noise.
- `changed_bytes_ratio` (float): fraction of bytes changed across the overlapping prefix.
- `delta_size_ratio` (float, optional): (size(Lk) − size(L0)) / size(L0); defaults to 0.0 if missing.
- Metadata: `class`, `sha256`, `level`, `obf_type`, `compare`.

Rows missing `jsd_vs_L0` are dropped. Only L0-paired rows are scored.

## Normalization (clipped to [0,1])
We scale each metric to a bounded 0..1 channel using pragmatic caps:
- `n_jsd       = clip(jsd_vs_L0 / 0.50)`
- `n_dH_pos    = clip(max(delta_entropy, 0) / 1.5)`
- `n_dD_pos    = clip(max(delta_diffstd, 0) / 5.0)`
- `n_changed   = clip(changed_bytes_ratio / 0.05)`
- `n_dsize     = clip(max(delta_size_ratio, 0) / 0.30)`

Interpretation: 0.50 JSD, +1.5 bits entropy, +5.0 diffstd, +5% bytes-changed, and +30% size growth each saturate their channels at 1.0. Negative deltas on entropy/diffstd/size contribute 0.

## Composite score
```
challenge_score = w_jsd*n_jsd + w_dH*n_dH_pos + w_dD*n_dD_pos + w_changed*n_changed + w_dsize*n_dsize
```
Default weights (CLI-tunable):
- `w_jsd=0.45`, `w_dH=0.20`, `w_dD=0.20`, `w_changed=0.10`, `w_dsize=0.0`
  (corrected this pass — tracked artifact provenance records `0.0`, not the
  `0.05` previously documented here; the size-delta channel currently
  contributes nothing to the composite score).

## Lane labeling (challenge_label)
After scoring, assign a label per pair:
- L3 (XOR-like) if either:
  - `obf_type` matches `(?i)(xor|blockxor|upx)`, or
  - `delta_diffstd < 0.0` AND `jsd_vs_L0 ≥ 0.15`.
- Else L2 candidate if ALL true:
  - `0.01 ≤ jsd_vs_L0 < 0.45`,
  - `changed_bytes_ratio ≥ l2_min_changed` (default `0.008`),
  - `delta_diffstd ≥ 0.0`.
  - Within L2: `L2_strong` if `challenge_score ≥ tau_l2` (default `0.10`), else `L2_weak`.
- Else `L1`.

Provenance JSON (`source_note`) is embedded when writing outputs, including weights, thresholds, pairing mode, and coverage controls.

## Outputs
- `challenge_score.csv`: per-pair score, normalized channels, and label.
- `challenge_counts.csv` and `challenge_counts_unique.csv`: counts by class/level/obf/label (raw and deduped by (class,sha256,level)).

## Defaults and CLI flags
The weights and gates above are the defaults used by the generator. An
earlier version of this document cited a `tools/binary_diversity.py` and an
image-based variant script as their source; neither exists in this repo.
The actual generator is `scripts/recompute_jsd_from_manifest.py` in the
private working repo.

## Notes and caveats
- Only strict L0 pairings are scored; ensure `compare` begins with `L0-`.
- Clipping caps reflect practical saturation points and are adjustable if distributions shift.
- Negative `delta_diffstd` with high JSD is treated as an XOR-like cue when obf strings are unreliable.

## Suggested locations
- This doc: `obfuscale/docs/jsd_challenge_score.md` (current).
- If you prefer co-locating with code, a short `README.md` section under `tools/` (near `binary_diversity.py`) can link back here.
