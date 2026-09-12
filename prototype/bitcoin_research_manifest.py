"""Manifeste deterministe pour reproduire une analyse Bitcoin."""
import hashlib
import unittest
def manifest(source,revision,files): return hashlib.sha256((source+"|"+revision+"|"+",".join(sorted(files))).encode()).hexdigest()
class Tests(unittest.TestCase):
 def test_order_does_not_change_manifest(self): self.assertEqual(manifest("core","main",["a","b"]),manifest("core","main",["b","a"]))
 def test_revision_is_bound(self): self.assertNotEqual(manifest("core","main",["a"]),manifest("core","v2",["a"]))
if __name__=="__main__": unittest.main()
