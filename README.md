# WEASEL — EFMW Zoo #32

**Weakness Exploration through Adversarial Search, Exploitation & Limits**

WEASEL is an experimental EFMW-inspired red-team framework for systematically searching for brittle assumptions, unsafe edge cases, and unexpected paths around controls in a bounded test environment.

## Core question

> What is the smallest admissible perturbation that exposes a real weakness in the system?

WEASEL is designed for defensive evaluation. It does not include destructive payloads, credential theft, persistence, malware behavior, or unauthorized exploitation.

## Primary outputs

- weakness discovery rate
- exploit-path length
- control-bypass score
- perturbation efficiency
- reproducibility
- severity estimate
- mitigation coverage
- residual attack surface

## Repository contents

- `theory.md`
- `architecture.md`
- `adversarial_model.md`
- `limitations.md`
- `weasel.py`
- `benchmark.py`
- `ablations.py`
- `test_weasel.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_weasel.py
```

## Zoo position

BISON #31 stress-tests integrity under overload.

**WEASEL #32 actively searches for the narrow cracks that remain when the system appears to be working normally.**
