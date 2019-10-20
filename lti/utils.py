from collections import UserDict
import json

class LTIDict(dict):

    unshort ={
        "deployment_id": "https://purl.imsglobal.org/spec/lti/claim/deployment_id",
        "message_type": "https://purl.imsglobal.org/spec/lti/claim/message_type",
        "version": "https://purl.imsglobal.org/spec/lti/claim/version",
        "role": "https://purl.imsglobal.org/spec/lti/claim/roles",
        "context": "https://purl.imsglobal.org/spec/lti/claim/context",
        "resource_link": "https://purl.imsglobal.org/spec/lti/claim/resource_link",
        "tool_platform": "https://purl.imsglobal.org/spec/lti/claim/tool_platform",
        "launch_presentation": "https://purl.imsglobal.org/spec/lti/claim/launch_presentation",
        "custom": "https://purl.imsglobal.org/spec/lti/claim/custom",
        "deep_linking_settings": "https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings",
        "content_items": "https://purl.imsglobal.org/spec/lti-dl/claim/content_items"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __getitem__(self, key):
        uk = LTIDict.unshort.get(key,key)
        v = self.get(uk)
        if (v and isinstance(v, dict)):
            v = LTIDict(**v)              
        return v

    def __setitem__(self, key, val):
        super().__setitem__(LTIDict.unshort.get(key, key), val)

    def __getattr__(self, key):
        return self.__getitem__(key)
