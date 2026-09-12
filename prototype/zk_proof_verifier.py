"""ZK proof : verification finale d un paquet minimal."""
import hashlib
import unittest
def digest(trace,claim,root): return hashlib.sha256((root+":"+str(claim)+":"+",".join(map(str,trace))).encode()).hexdigest()
def verify(trace,claim,root,proof): return bool(trace) and proof==digest(trace,claim,root)
class Tests(unittest.TestCase):
 def test_valid_package(self):
  t=[2,5,8]; p=digest(t,8,"root")
  self.assertTrue(verify(t,8,"root",p))
 def test_changed_claim_rejected(self):
  t=[2,5,8]; p=digest(t,8,"root")
  self.assertFalse(verify(t,9,"root",p))
 def test_empty_trace_rejected(self): self.assertFalse(verify([],0,"root","x"))
if __name__=="__main__": unittest.main()
