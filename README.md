<p align="center">
  <picture>
    <!-- Dark mode: show the LIGHT logo -->
    <source media="(prefers-color-scheme: dark)" 
            srcset="docs/assets/obfuscale-logo-light.png">
    <!-- Light mode (default): show the DARK logo -->
    <source media="(prefers-color-scheme: light)" 
            srcset="docs/assets/obfuscale-logo-dark.png">
    <img alt="ObfuScale" src="docs/assets/obfuscale-logo-dark.png" height="72">
  </picture>
</p>

# ObfuScale

ObfuScale is a framework for measuring how binary-to-image CNN malware 
detection models respond to obfuscation. It defines a byte-level 
obfuscation ladder (L0–L3), converts binaries into byteplot images, and 
evaluates convolutional neural networks (ResNet, ConvNeXt) across 
representation choices and exposure policies. A Jensen–Shannon-divergence 
based "challenge score" measures how much an obfuscated variant's byte 
distribution diverges from its original — a descriptive statistic about 
the transform, not a validated predictor of detection difficulty.

## Status

Pre-release, under active rework. An earlier version of this repository 
shipped a demo command that wrote fabricated benchmark metrics, and 
documented an obfuscation ladder whose L1/L2 levels were byte-identical 
to L0 due to an implementation bug. Both issues are being corrected as 
part of a from-scratch, honestly-reported rerun of the pipeline; this 
README will be updated to reflect real results once they exist. Core 
pipeline code (`src/obfuscale/`) is currently unimplemented scaffolding.

## Research Context

ObfuScale originated from the following SANS Technology Institute 
master's thesis:

> Reglein, M. (2025). *Measuring Malware Obfuscation: Evaluating 
> CNN-Based Detection for Real-World Resilience.* SANS Technology 
> Institute. https://www.sans.edu/cyber-research/measuring-malware-obfuscation-evaluating-cnn-based-detection-real-world-resilience/

The platform measures how binary-to-image CNN malware detection models 
perform as obfuscation levels increase, using a subset of the SOREL-20M 
dataset.

## What's Here Now

- `src/obfuscale/` — package scaffolding (challenge scoring, image pipeline, baseline CNN); these modules are currently stubs, not working implementations
- `docs/` — methodology notes and repo layout
- `env/` — environment specification

## Coming Soon

- Full canonical pipeline scripts
- Jupyter notebook walkthrough
- Seed model weights
- Complete methodology and parameter documentation
- Extension guidance for new obfuscation methods and model architectures

## Dataset

Developed using a subset of SOREL-20M. Binaries are not distributed — 
hashes and references will be provided for reproducibility.

## License

Copyright 2025 Michael Reglein

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) 
for details.
