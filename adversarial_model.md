# Adversarial Model

## Safe evaluation boundary

WEASEL operates only on:
- local test functions,
- synthetic systems,
- sandboxed applications,
- explicitly authorized evaluation targets.

It does not provide:
- destructive exploit payloads,
- credential harvesting,
- persistence techniques,
- malware,
- stealth or evasion for unauthorized access.

## Candidate schema

```json
{
  "id": "p17",
  "changes": {
    "timeout": 0,
    "retry_count": 5
  },
  "magnitude": 0.22,
  "authorized": true
}
```

## Finding schema

```json
{
  "weakness_id": "w3",
  "severity": 0.7,
  "reproducibility": 0.9,
  "path_length": 2,
  "control_bypass": 0.5,
  "mitigation_status": "open"
}
```

## Search policy

Search operators may include:
- bounded numeric mutation,
- categorical substitution,
- ordering permutation,
- omission,
- duplication,
- contradictory-but-valid test inputs.

## Stopping conditions

Stop when:
- budget exhausted,
- severity threshold reached,
- no improvement for N iterations,
- safety boundary would be exceeded.
