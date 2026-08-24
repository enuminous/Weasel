from dataclasses import dataclass
from typing import Callable, Dict, List, Any, Optional
import itertools
import copy

@dataclass
class Finding:
    perturbation: Dict[str, Any]
    severity: float
    cost: float
    reproducibility: float
    explanation: str

class WeaselSearch:
    def __init__(
        self,
        target: Callable[[Dict[str, Any]], Any],
        weakness_predicate: Callable[[Any], float],
        allowed_values: Dict[str, List[Any]],
        base_input: Dict[str, Any],
        max_changes: int = 2
    ):
        self.target = target
        self.weakness_predicate = weakness_predicate
        self.allowed_values = allowed_values
        self.base_input = copy.deepcopy(base_input)
        self.max_changes = max_changes

    def perturbations(self):
        keys = list(self.allowed_values)
        yield {}
        for k in range(1, self.max_changes + 1):
            for chosen in itertools.combinations(keys, k):
                pools = [self.allowed_values[c] for c in chosen]
                for vals in itertools.product(*pools):
                    p = dict(zip(chosen, vals))
                    changed = {
                        key: val for key, val in p.items()
                        if self.base_input.get(key) != val
                    }
                    if changed:
                        yield changed

    def cost(self, perturbation):
        if not perturbation:
            return 0.0
        return len(perturbation) / max(1, len(self.base_input))

    def run_case(self, perturbation):
        case = copy.deepcopy(self.base_input)
        case.update(perturbation)
        result = self.target(case)
        severity = float(self.weakness_predicate(result))
        return case, result, max(0.0, severity)

    def reproduce(self, perturbation, trials=3):
        success = 0
        for _ in range(trials):
            _, result, severity = self.run_case(perturbation)
            if severity > 0:
                success += 1
        return success / trials

    def search(self, top_n=5):
        findings = []
        seen = set()

        for p in self.perturbations():
            key = tuple(sorted(p.items()))
            if key in seen:
                continue
            seen.add(key)

            _, result, severity = self.run_case(p)
            if severity <= 0:
                continue

            r = self.reproduce(p)
            findings.append(Finding(
                perturbation=p,
                severity=severity,
                cost=self.cost(p),
                reproducibility=r,
                explanation=f"Authorized bounded case produced severity {severity:.3f}"
            ))

        findings.sort(key=lambda f: (-f.severity, f.cost, -f.reproducibility))
        return findings[:top_n]
