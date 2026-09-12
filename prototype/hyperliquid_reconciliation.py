"""Hyperliquid : reconciliation d etat local et observe."""
import unittest
def diff(expected,observed): return sorted(set(expected)^set(observed))
class Tests(unittest.TestCase):
 def test_equal(self): self.assertEqual(diff(["a","b"],["b","a"]),[])
 def test_missing_is_reported(self): self.assertEqual(diff(["a","b"],["a"]),["b"])
if __name__=="__main__": unittest.main()
