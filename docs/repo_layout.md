ObfuScale/
├─ README.md                     # landing page (portfolio + reproduce links)
├─ LICENSE                       # Apache-2.0
├─ NOTICE                        # dataset + attribution notes
├─ .gitignore                    # blocks data, outputs, secrets
├─ env/
│  ├─ environment.yml            # conda spec
│  └─ pre-commit-config.yaml     # black/ruff/nbstripout + detect-secrets
├─ src/
│  └─ obfuscale/
│     ├─ __init__.py
│     ├─ cli.py                  # Typer entrypoint: `obfuscale …`
│     ├─ image_pipeline/         # bin→image (head/tail/HTS) + size ops
│     │  ├─ __init__.py
│     │  ├─ windowing.py
│     │  └─ byteplot.py
│     ├─ challenge_score/        # JSD + bootstrap utilities
│     │  ├─ __init__.py
│     │  └─ jsd.py
│     └─ models/                 # light runners (ResNet/ConvNeXt wrappers)
│        ├─ __init__.py
│        └─ cnn_baseline.py
├─ configs/
│  ├─ paths.example.yaml         # copy to paths.yaml (gitignored)
│  └─ runs/
│     └─ baseline.yaml           # tiny deterministic demo
├─ orchestrate/
│  ├─ Makefile                   # setup, lint, baseline, docs
│  └─ tasks.md                   # one-line commands cheat sheet
├─ data/
│  ├─ README.md                  # “how to get SOREL, benign, where to place”
│  └─ manifests/                 # tiny safe manifests (hashes/metadata only)
├─ results/
│  ├─ README.md                  # what lands here, what is committed
│  └─ baseline/                  # small artifacts OK to commit
├─ notebooks/
│  ├─ 01_ember_images_demo.ipynb # curated demo, stripped outputs
│  └─ 02_challenge_score.ipynb   # small JSD demo
└─ .github/
   └─ workflows/
      └─ ci.yml                  # ruff/black + docs build (fast)

What each of the above does:

    src/obfuscale/: importable library + one CLI to run demos (make baseline).

    image_pipeline/: windowing choices (Head, Head–Tail, HTS) + byte→PNG.

    challenge_score/: JSD + bootstrap; validates L0 vs L1/L3 separation.

    models/: tiny CNN runner to generate a baseline ROC/metrics without heavy infra.

    configs/: all knobs live here; paths are local in a user-copied paths.yaml.

    orchestrate/Makefile: the single source of truth for commands.

    data/: no binaries; only manifests and docs.

    results/baseline/: tiny committed outputs (e.g., confusion matrix PNG, metrics.csv).

    notebooks/: ≤2 curated, output-stripped notebooks for readers.

Additional docs:

   docs/jsd_challenge_score.md: canonical description of the binary JSD challenge score formula and labeling.

Nice to have:
docs/                               # MkDocs (dual-track docs)
├─ index.md
├─ quick-tour/
│  ├─ 01_problem.md
│  ├─ 02_approach.md
│  └─ 03_results.md
├─ reproduce/
│  ├─ 01_env.md
│  ├─ 02_data_layout.md
│  └─ 03_run_baseline.md
└─ evolution/
   ├─ collapse-l1-l2.md
   ├─ head-tail-256.md
   └─ obfuscation-aware-calibration.md
mkdocs.yml                          # optional if you want Pages
CITATION.cff                        # scholarly citation block
SECURITY.md                         # responsible use, no malicious use
SYNC.md                             # Gitea→GitHub commands + checklist
tests/                              # unit tests for jsd windowing & CLI I/O
pyproject.toml                      # ruff/black/isort/pytest config in one place
