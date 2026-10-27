# WEASEL — EFMW Zoo #32

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Weasel) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Core question](#core-question)
- [Primary outputs](#primary-outputs)
- [Repository contents](#repository-contents)
- [Quick start](#quick-start)
- [Zoo position](#zoo-position)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Salmon](https://github.com/enuminous/Salmon) · [Bison](https://github.com/enuminous/Bison) · [Orca](https://github.com/enuminous/Orca) · [Mantis](https://github.com/enuminous/Mantis)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
