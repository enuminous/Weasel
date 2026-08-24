import unittest
from weasel import WeaselSearch

def target(cfg):
    if cfg["a"] == 0 and cfg["b"] == 0:
        return {"sev":1.0}
    if cfg["a"] == 0:
        return {"sev":0.3}
    return {"sev":0.0}

class TestWeasel(unittest.TestCase):
    def make(self, max_changes=2):
        return WeaselSearch(
            target=target,
            weakness_predicate=lambda r:r["sev"],
            allowed_values={"a":[1,0],"b":[1,0]},
            base_input={"a":1,"b":1},
            max_changes=max_changes
        )

    def test_finds_weakness(self):
        out = self.make().search()
        self.assertTrue(len(out) > 0)

    def test_multi_change_finds_higher_severity(self):
        one = self.make(1).search()
        two = self.make(2).search()
        self.assertGreater(max(f.severity for f in two),
                           max(f.severity for f in one))

    def test_reproducibility(self):
        out = self.make().search()
        self.assertEqual(out[0].reproducibility, 1.0)

if __name__ == "__main__":
    unittest.main()
