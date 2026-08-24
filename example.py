from weasel import WeaselSearch

def target(cfg):
    # Fully local toy validator.
    if cfg["limit"] == 0 and cfg["fallback"] is False:
        return {"severity":0.8, "status":"unsafe state"}
    return {"severity":0.0, "status":"ok"}

search = WeaselSearch(
    target=target,
    weakness_predicate=lambda r: r["severity"],
    allowed_values={
        "limit":[10,1,0],
        "fallback":[True,False]
    },
    base_input={
        "limit":10,
        "fallback":True
    },
    max_changes=2
)

for finding in search.search():
    print(finding)
