# WEASEL: Weakness Exploration through Adversarial Search, Exploitation & Limits

## Abstract

WEASEL is an experimental defensive red-team framework for searching bounded perturbation spaces for reproducible system weaknesses. It prioritizes minimal, explainable test cases and explicitly separates authorized evaluation from destructive exploitation.

## 1. Motivation

Many defects appear only under narrow combinations of valid but unusual conditions.

Random testing may miss these combinations.

WEASEL searches them deliberately.

## 2. Model

Authorized perturbation space:

`P_safe`

Weakness predicate:

`W(x,p)`

Search objective:

`J(p)=severity(W)-lambda*cost(p)`

A preferred finding is:
- severe,
- low cost,
- short path,
- reproducible,
- causally interpretable.

## 3. Metrics

- discovery rate
- minimum perturbation cost
- path length
- reproducibility
- severity
- mitigation closure rate
- residual attack surface

## 4. Baselines

- random fuzzing
- property-based testing
- combinatorial testing
- mutation testing
- conventional red-team checklists

## 5. Ablations

- single-step search only
- no minimization
- no reproducibility check
- random perturbation ordering
- no state history
- no severity weighting

## 6. Falsification

If conventional fuzzing and property testing find equal or better defects at lower cost under the same authorized conditions, WEASEL's added search structure is not justified.

## 7. Safety boundary

This repository is intentionally limited to defensive, local, synthetic, or explicitly authorized testing. It does not contain destructive payloads, unauthorized access techniques, malware, credential theft, persistence, or stealth mechanisms.

## 8. Claim boundary

Finding no weaknesses does not establish security. WEASEL evaluates only the explored test space.
