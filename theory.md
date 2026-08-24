# WEASEL Theory

## 1. Problem

Many systems fail only under carefully chosen edge cases.

Examples:
- unusual input combinations,
- conflicting constraints,
- sequence-dependent behavior,
- hidden assumptions,
- boundary-condition errors,
- policy gaps,
- untested state transitions.

WEASEL treats defensive red-teaming as a structured search problem.

## 2. Search space

Let admissible perturbations be:

`p in P_safe`

where `P_safe` is explicitly bounded by the evaluation policy.

The tested system maps:

`y = F(x, p)`

## 3. Weakness condition

Define a weakness predicate:

`W(x,p) in {0,1}`

Examples:
- invariant violation,
- incorrect output,
- policy inconsistency,
- crash,
- unsafe state transition,
- unhandled contradiction.

## 4. Search objective

A candidate search objective:

`J(p) = severity(W) - lambda*cost(p) - gamma*distance(p,p0)`

This favors small, reproducible perturbations that reveal meaningful defects.

## 5. Minimal exploit path

For a sequence:

`P = [p1, p2, ..., pk]`

define path length `k`.

WEASEL prefers:
- shorter paths,
- lower perturbation magnitude,
- higher reproducibility,
- clearer causal attribution.

## 6. Control bypass

For control set `C`, measure:

`B = number_of_controls_bypassed / number_of_relevant_controls`

A bypass only counts if the test remains within the authorized harness.

## 7. Reproducibility

For repeated trials:

`R = successful_reproductions / total_trials`

Low reproducibility lowers confidence in the finding.

## 8. Residual attack surface

After mitigation `m`:

`A_residual = weaknesses_after / weaknesses_before`

Lower is better.

## 9. EFMW interpretation

The EFMW-inspired aspect is recursive adversarial search with explicit state tracking:
- what was tried,
- what changed,
- which control failed,
- what evidence supports the failure,
- whether the failure persists after mitigation.

## 10. Falsifiable prediction

WEASEL should add value when:
- weaknesses are sequence-dependent,
- the search space is combinatorial,
- boundary cases matter,
- simple fuzzing misses relational defects.

If standard fuzzing, property testing, and conventional red-team suites find the same issues at lower cost, WEASEL is not justified.
