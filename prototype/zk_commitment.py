"""ZK proof : engagement deterministe d une trace."""
import hashlib
import unittest
def commit(trace,salt=""): return hashlib.sha256((salt+":"+",".join(map(str,trace))).encode()).hexdigest()
def opens(root,trace,salt=""): return root==commit(trace,salt)
class Tests(unittest.TestCase):
 def test_valid_opening(self): self.assertTrue(opens(commit([2,5,8],"s"),[2,5,8],"s"))
 def test_modified_trace_rejected(self): self.assertFalse(opens(commit([2,5,8],"s"),[2,6,8],"s"))
 def test_domain_salt_matters(self): self.assertNotEqual(commit([1],"a"),commit([1],"b"))
if __name__=="__main__": unittest.main()
