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

ObfuScale provides a consistent "yardstick" for measuring the impact of 
obfuscation on malware detection models. It introduces a reproducible 
obfuscation ladder (L0–L3), converts binaries into byteplot images, and 
benchmarks convolutional neural networks (ResNet, ConvNeXt) across 
representation choices and exposure policies. The framework validates 
obfuscation difficulty using a challenge score based on Jensen–Shannon 
divergence, ensuring that each level reflects a measurable increase in 
complexity.

## Status

Active development. This repository is being prepared for full public 
release. Core pipeline, documentation, and reproducibility materials 
are being finalized.

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

- `src/obfuscale/` — core package (challenge scoring, image pipeline, baseline CNN)
- `docs/` — methodology notes and repo layout
- `configs/` — example configuration structure
- `env/` — reproducible environment specification

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
