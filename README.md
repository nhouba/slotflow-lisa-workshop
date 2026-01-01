# SlotFlow LISA Workshop: ML for Galactic Binary Search & Parameter Estimation

Hands-on tutorials for applying machine learning to LISA gravitational wave detection of Galactic Binaries (GBs), using [SlotFlow](https://github.com/nhouba/slotflow-inference) as a starting point.

## Overview

These tutorials were developed for a 2.5-day workshop on ML methods for LISA Galactic Binary analysis. They demonstrate key challenges and techniques that transfer to real LISA data analysis, while using SlotFlow's toy model (sinusoids at 2.5-3 Hz) for fast iteration.

**Important**: SlotFlow is a proof-of-concept demonstrating trans-dimensional inference with normalizing flows. The *methods* transfer to real LISA analysis; the specific frequency range and parameter space do not.

| Tutorial | Topic | Duration |
|----------|-------|----------|
| 00 | Setup & Quick Start | ~15 min |
| 01 | Confusion Regime Mapping | ~30 min |
| 02 | Verification Binaries | ~30 min |
| 03 | Toward Realistic Data | ~30 min |
| 04 | Benchmarking & Metrics | ~30 min |
| 05 | ML to MCMC Initialization | ~30 min |

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/slotflow-workshop.git
cd slotflow-workshop
```

### 2. Create environment and install dependencies

```bash
# Using conda (recommended)
conda create -n slotflow-workshop python=3.11
conda activate slotflow-workshop

# Install dependencies
pip install -r requirements.txt
```

### 3. Download the pretrained model

Download the pretrained SlotFlow model from the [v1.0.0 release](https://github.com/nhouba/slotflow-inference/releases/tag/v1.0.0):

```bash
# Create model directory
mkdir -p pretrained_model/test_clariden/checkpoints

# Download model files (adjust URLs based on actual release assets)
# Option 1: Using the download script
python download_model.py

# Option 2: Manual download
# Download best_model.ckpt and model_config.pt from the release page
# and place them in pretrained_model/test_clariden/
```

Alternatively, clone the full SlotFlow repository which includes the pretrained model:

```bash
git clone https://github.com/nhouba/slotflow-inference.git
cp -r slotflow-inference/pretrained_model .
```

### 4. Run the tutorials

```bash
cd notebooks
jupyter notebook
```

## Tutorial Descriptions

### Tutorial 00: Setup & Quick Start
Foundation tutorial that loads the SlotFlow model, runs basic inference, and explains the mapping between the toy model and real LISA GBs.

### Tutorial 01: Confusion Regime Mapping
Systematically explore where ML methods fail by sweeping frequency separation (Δf), SNR, and number of sources (K). Creates confusion maps to identify challenging parameter regimes.

### Tutorial 02: Verification Binaries
Test inference on verification binary (VB) parameters - known astrophysical sources with electromagnetic counterparts. Demonstrates how to scale real VB properties to the toy model.

### Tutorial 03: Toward Realistic Data
Extend the signal model toward LISA reality:
- Add frequency derivatives (chirping signals)
- Introduce sky-position-dependent modulation
- Scaffold for adding more realistic noise models

### Tutorial 04: Benchmarking & Metrics
Define proper evaluation metrics for GB ML methods:
- Calibration diagnostics (are credible intervals honest?)
- Wasserstein distance to reference posteriors
- Comprehensive benchmark suite design

Uses Hungarian matching for proper slot-to-source alignment.

### Tutorial 05: ML to MCMC Initialization
Hybrid approach combining ML speed with MCMC rigor:
- Extract point estimates and covariances from SlotFlow
- Initialize Metropolis-Hastings with ML results
- Measure burn-in reduction and ESS improvement

## Key Concepts

### Hungarian Matching
SlotFlow outputs are permutation-invariant (slot order is arbitrary). To compare predictions with ground truth, we use Hungarian matching based on flow log-probability - the same matching used during training.

### Toy Model vs LISA Reality

| Aspect | SlotFlow (Toy) | Real LISA GBs |
|--------|---------------|---------------|
| Frequency range | 2.5-3.0 Hz | 0.1-30 mHz |
| Parameters/source | 3 (A, φ, f) | 7-8 (f, ḟ, A, ι, ψ, φ₀, λ, β) |
| Observation time | 300 s | 4+ years |
| Number of sources | 1-10 | ~10,000 resolvable |

### What Transfers
- Trans-dimensional inference (learning K)
- Slot-based architecture for variable source counts
- Hungarian matching for permutation invariance
- Normalizing flows for posterior estimation
- Dual-stream encoding (time + frequency domain)

## Project Ideas

Each tutorial includes extension ideas suitable for workshop projects:

1. **Extend confusion mapping** to higher K, different noise models
2. **Full VB catalog analysis** with realistic parameter distributions
3. **Implement chirping + sky modulation** together
4. **Add precision/recall metrics** for source detection
5. **Interface with Eryn/emcee** for production MCMC

## References

- **SlotFlow Paper**: [arXiv:2511.23228](https://arxiv.org/abs/2511.23228)
- **SlotFlow Code**: [github.com/nhouba/slotflow-inference](https://github.com/nhouba/slotflow-inference)
- **Pretrained Model**: [v1.0.0 Release](https://github.com/nhouba/slotflow-inference/releases/tag/v1.0.0)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Citation

If you use these tutorials or SlotFlow in your research, please cite:

```bibtex
@misc{houba2025slotflow,
      title={SlotFlow: Amortized Trans-Dimensional Inference with Slot-Based Normalizing Flows}, 
      author={Niklas Houba and Giovanni Giarda and Lorenzo Speri},
      year={2025},
      eprint={2511.23228},
      archivePrefix={arXiv},
      primaryClass={astro-ph.IM},
      url={https://arxiv.org/abs/2511.23228}, 
}
```
