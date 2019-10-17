from collections import UserDict

class LTIMessage(UserDict):

    short = {
        "https://purl.imsglobal.org/spec/lti/claim/deployment_id": "deployment_id",
        "https://purl.imsglobal.org/spec/lti/claim/message_type": "message_type",
        "https://purl.imsglobal.org/spec/lti/claim/version": "version",
        "https://purl.imsglobal.org/spec/lti/claim/roles": "role",
        "https://purl.imsglobal.org/spec/lti/claim/context": "context",
        "https://purl.imsglobal.org/spec/lti/claim/resource_link": "resource_link",
        "https://purl.imsglobal.org/spec/lti/claim/tool_platform": "tool_platform",
        "https://purl.imsglobal.org/spec/lti/claim/launch_presentation": "launch_presentation",
        "https://purl.imsglobal.org/spec/lti/claim/custom": "custom",
        "https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings": "deep_linking_settings",
        "https://purl.imsglobal.org/spec/lti-dl/claim/content_items": "content_items"
    }

    unshort = {v: k for k, v in short.items()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        d = self.data
        for k in key.split('.'):
            if isinstance(d, dict):
                d = d.get(LTIMessage.unshort.get(k, k))
        return d

    def __setitem__(self, key, val):
        self.data.__setitem__(LTIMessage.unshort.get(key, key), val)