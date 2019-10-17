import unittest

from lti.messages import LTIMessage

class LTIPlatformTest(unittest.TestCase):

    def setUp(self):
        d = {
            "https://purl.imsglobal.org/spec/lti/claim/version": "1.3.0",
            "sub": "33232",
            "https://purl.imsglobal.org/spec/lti/claim/resource_link": {
                "id": "200d101f",
                "description": "Assignment to introduce who you are",
                "title": "Introduction Assignment"
            },
            "https://purl.imsglobal.org/spec/lti-dl/claim/content_items": [
                {
                    "type": "link",
                    "title": "My Home Page",
                    "url": "https://something.example.com/page.html",
                    "icon": {
                        "url": "https://lti.example.com/image.jpg",
                        "width": 100,
                        "height": 100
                    },
                    "thumbnail": {
                        "url": "https://lti.example.com/thumb.jpg",
                        "width": 90,
                        "height": 90
                    }
                }]
        }
        self.message = LTIMessage(d)

    def test_get(self):
        self.assertEqual(self.message['version'], "1.3.0")
        self.assertEqual(self.message['content_items'][0]["type"], "link")
        self.assertEqual(self.message['resource_link.id'], "200d101f")

    def test_str(self):
        m = LTIMessage([])
        m['version']='1.3.0'
        self.assertEqual('{\'https://purl.imsglobal.org/spec/lti/claim/version\': \'1.3.0\'}', str(m))

