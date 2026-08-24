from weasel import WeaselSearch
from benchmark import toy_system, weakness

def run(max_changes):
    s = WeaselSearch(
        target=toy_system,
        weakness_predicate=weakness,
        allowed_values={
            "threshold": [1,0,-1],
            "retries": [0,1,3],
            "mode": ["safe","fast"]
        },
        base_input={"threshold":1,"retries":0,"mode":"safe"},
        max_changes=max_changes
    )
    return s.search(10)

if __name__ == "__main__":
    one = run(1)
    three = run(3)
    print("single-change best severity:", max([f.severity for f in one], default=0))
    print("multi-change best severity:", max([f.severity for f in three], default=0))
