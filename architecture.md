# WEASEL Architecture

## Pipeline

1. Test Policy Loader
2. Input/State Encoder
3. Perturbation Generator
4. Constraint Guard
5. Test Executor
6. Weakness Predicate Evaluator
7. Severity Scorer
8. Reproducer
9. Minimizer
10. Mitigation Retest Loop

## Inputs

- authorized target or local function
- valid input domain
- invariants
- safety boundaries
- mutation budget
- severity rules

## Outputs

```json
{
  "finding": true,
  "severity": 0.72,
  "path_length": 1,
  "perturbation_cost": 0.08,
  "reproducibility": 1.0,
  "minimized_case": {
    "threshold": -1
  }
}
```

## Design principle

WEASEL is not rewarded for causing arbitrary failure.

It is rewarded for finding the **smallest explainable authorized test case** that exposes a genuine defect.

## Integration

MAGPIE can audit evidence for findings.

ELEPHANT can preserve the complete red-team history.

BEAVER can test proposed fixes.

BISON can test whether mitigations survive overload.
