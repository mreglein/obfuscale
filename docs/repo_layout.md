# Repo layout

This describes what actually exists in this repository today, not a target
structure. It will be updated as the pipeline is rebuilt.

```
obfuscale-public/
├─ README.md              # landing page
├─ LICENSE                # Apache-2.0
├─ NOTICE                 # dataset + attribution notes
├─ env/
│  └─ environment.yml     # conda environment spec
├─ requirements.txt       # pip environment spec
├─ src/
│  └─ obfuscale/
│     ├─ __init__.py
│     ├─ cli.py               # Typer entrypoint; `baseline` is currently
│     │                       # a not-implemented stub (see Status in
│     │                       # the root README)
│     ├─ image_pipeline/
│     │  ├─ __init__.py
│     │  ├─ windowing.py      # partially implemented
│     │  └─ byteplot.py       # unimplemented stub
│     ├─ challenge_score/
│     │  ├─ __init__.py
│     │  └─ jsd.py            # unimplemented stub; the working JSD/
│     │                       # challenge-score code lives in the private
│     │                       # working repo pending its own remediation
│     └─ models/
│        ├─ __init__.py
│        └─ cnn_baseline.py   # unimplemented stub
└─ docs/
   ├─ repo_layout.md      # this file
   └─ jsd_challenge_score.md  # challenge-score methodology notes
```

No `configs/`, `data/`, `results/`, `notebooks/`, `tests/`, or `.github/`
directories exist in this repository yet. `docs/jsd_challenge_score.md`
describes a metric that has not yet been validated as predictive of
detection difficulty — read it as a description of what is computed, not
a claim about what it means.
