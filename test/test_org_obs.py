import unittest
import sys
sys.path.insert(0, '/home/mrweckx/Proyectos/org_obs')
# sys.append('/home/mrweckx/Proyectos/org_obs')
from org_obs import OrgObs


class TesttoTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(True, True)

    def test_paths_not_null(self):
        ob=OrgObs()
        res=ob.paths_not_null()
        self.assertEqual(True, res)


if __name__ == '__main__':
    unittest.main()
