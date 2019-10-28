import unittest

from lti.gen_model import LTIResourceLink

class LTIPlatformTest(unittest.TestCase):

    def test_resourcelink_attr(self):
        rl = LTIResourceLink()
        rl.max_points = 12.5
        self.assertEqual(rl.max_points, 12.5)
        self.assertEqual(rl['lineItem']['scoreMaximum'], 12.5)
