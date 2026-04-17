# Obfuscale pipeline

Local-only obfuscation experiment pipeline on Hermes.

Steps:
- Export Tier-0 manifest from config.data paths.
- Materialize cleanset via hard links into `artifacts/cleanset/files`.
- Generate L1/L2/L3 variants with deterministic naming and JSON sidecars.
- Upsert artifacts into repo-local `obfuscale.db`.
- Recompute JSD metrics and challenge scores.
- Render 2×2 panels and publish sanitized manifests.

See `../Makefile` for targets.
