from weasel import WeaselSearch

def toy_system(cfg):
    # Synthetic local target: invalid behavior emerges only in a narrow combination.
    threshold = cfg["threshold"]
    retries = cfg["retries"]
    mode = cfg["mode"]

    if threshold < 0 and retries >= 3 and mode == "fast":
        return {"ok": False, "severity": 1.0, "reason": "invariant violated"}
    if threshold < 0:
        return {"ok": False, "severity": 0.4, "reason": "bad threshold handling"}
    return {"ok": True, "severity": 0.0, "reason": "normal"}

def weakness(result):
    return result["severity"]

def run():
    search = WeaselSearch(
        target=toy_system,
        weakness_predicate=weakness,
        allowed_values={
            "threshold": [1, 0, -1],
            "retries": [0, 1, 3],
            "mode": ["safe", "fast"]
        },
        base_input={"threshold": 1, "retries": 0, "mode": "safe"},
        max_changes=3
    )
    return search.search(top_n=10)

if __name__ == "__main__":
    for f in run():
        print(f)
