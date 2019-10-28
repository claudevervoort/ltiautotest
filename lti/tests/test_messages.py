import unittest

from lti.messages import LTIMessageDict

class LTIPlatformTest(unittest.TestCase):

    def setUp(self):
        d = {
            "https://purl.imsglobal.org/spec/lti/claim/version": "1.3.0",
            "https://purl.imsglobal.org/spec/lti/claim/message_type": "LtiResourceLinkRequest",
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
        self.assertEqual(self.message.message_type, 'LtiResourceLinkRequest')
        self.message = LTIMessageDict(**d)

    def test_get(self):
        self.assertEqual(self.message['version'], "1.3.0")
        self.assertEqual(self.message['content_items'][0]["type"], "link")
        self.assertEqual(self.message['resource_link']['id'], "200d101f")
        self.assertEqual(self.message['https://purl.imsglobal.org/spec/lti/claim/message_type'], 'LtiResourceLinkRequest')

    def test_str(self):
        m = LTIMessageDict([])
        m['version']='1.3.0'
        self.assertEqual('{\'https://purl.imsglobal.org/spec/lti/claim/version\': \'1.3.0\'}', str(m))
        m['bla']=2
        self.assertEqual(m['bla'], 2)
        self.message['version']='changed'
        self.assertEqual(self.message['version'], "changed")
        self.message['newfield']='new'
        self.assertEqual(self.message['newfield'], "new")

