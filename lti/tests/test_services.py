import unittest

from lti.services import merge, next

class ServicesTest(unittest.TestCase):

    def test_merge(self):
        a = {'a1':1,'m':[1,2]}
        b = {'b1':2,'m':[3,4]}
        c = merge(a,b)
        self.assertEqual(c['a1'],1)       
        self.assertEqual(c['b1'],2)       
        self.assertEqual(c['m'],[1,2,3,4])       

    def test_next_headers(self):
        self.assertFalse(next({}))
        self.assertFalse(next({'Link': '<https://one.example.com>; rel="preconnect", <https://two.example.com>; rel="preconnect", <https://three.example.com>; rel="preconnect"'}))
        self.assertEqual(next({'Link': '<https://one.example.com>; rel="preconnect", <https://two.example.com>; rel=next, <https://three.example.com>; rel="preconnect"'}), 'https://two.example.com')
        self.assertEqual(next({'Link': '<https://one.example.com>; rel="preconnect", <https://two.example.com>; rel="next", <https://three.example.com>; rel="preconnect"'}), 'https://two.example.com')