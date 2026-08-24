# Limitations and Falsification

WEASEL is an experimental defensive red-team framework.

## Limitations

- Search quality depends on the mutation operators.
- A missed weakness is not evidence of safety.
- Severity functions may be subjective.
- Sandboxed behavior may differ from deployment behavior.
- Search can overfit a particular implementation.
- Some weaknesses require domain knowledge unavailable to generic mutation.

## Falsification criteria

WEASEL's central hypothesis is weakened if:

1. Standard fuzzing finds equal or more defects at lower cost.
2. Property-based testing fully matches coverage.
3. Sequence-aware search adds no value.
4. Minimization does not improve interpretability.
5. Findings fail reproduction.
6. Gains disappear on held-out targets.

## Claim boundary

WEASEL is a bounded defensive evaluation framework. It does not establish that a system is secure, nor does it authorize testing against systems without permission.
