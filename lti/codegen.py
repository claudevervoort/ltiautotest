models = {
    'Context': {
    },
    'ResourceLink': {
    },
    'ToolPlatform': {
    },
    'LaunchPresentation': {
    },
    'Custom': {},
    'DeepLinkSettings': {},
    'LTIMessage': {
        "iss": [],
        "sub": [],
        "given_name": [],
        "deployment_id": ["https://purl.imsglobal.org/spec/lti/claim/deployment_id"],
        "message_type": ["https://purl.imsglobal.org/spec/lti/claim/message_type"],
        "version": ["https://purl.imsglobal.org/spec/lti/claim/version"],
        "role": ["https://purl.imsglobal.org/spec/lti/claim/roles", "List[str]"],
        "context": ["https://purl.imsglobal.org/spec/lti/claim/context", 'Context'],
        "resource_link": ["https://purl.imsglobal.org/spec/lti/claim/resource_link", 'ResourceLink'],
        "tool_platform": ["https://purl.imsglobal.org/spec/lti/claim/tool_platform", 'ToolPlatform'],
        "launch_presentation": ["https://purl.imsglobal.org/spec/lti/claim/launch_presentation", 'LaunchPresentation'],
        "custom": ["https://purl.imsglobal.org/spec/lti/claim/custom", 'Custom'],
        "deep_linking_settings": ["https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings", 'DeepLinkSettings'],
    },
    'DeeplinkResponse': {
        "content_items": ["https://purl.imsglobal.org/spec/lti-dl/claim/content_items", "List"]
    },
    'LineItem': {
        'label': [],
        'scoreMaximum': ['', 'float'],
        'tag':[],
        'resourceId': [],
        'resourceLinkId': []
    },
    'LTIResourceLink': {
        'type': ['', 'str', 'ltiResourceLink'],
        'title': [],
        'text': [],
        'url': [],
        'line_item': ['lineItem', 'LineItem'],
        'max_points': ['lineItem:LineItem->scoreMaximum', 'float'],
        'resource_id': ['lineItem:LineItem->resourceId', 'float']
    }
}

template_class = "class {name}(dict):"

template_class_init = """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
"""

template_class_init_val = """
        if not self.get('{long}'):
            self['{long}'] = '{value}'
"""

template_property = """
    @property
    def {short}(self) -> {type}:
        return self.get('{long}')

    @{short}.setter
    def {short}(self, value: {type}):
        self['{long}'] = value
"""

template_nested_property = """
    @property
    def {short}(self) -> {type}:
        if self.get('{container}'):
            return self.get('{container}').get('{attr}')

    @{short}.setter
    def {short}(self, value: {type}):
        if not self.get('{container}'):
            self['{container}'] = {container_class}()
        self['{container}']['{attr}'] = value
"""


def generate(name: str, spec: dict):
    gen = []
    gen.append(template_class.format(name=name))
    init = False
    for (k, v) in spec.items():
        if len(v) == 3:
            lk = k if len(v) == 0 or len(v[0]) == 0 else v[0]
            if not init:
                gen.append(template_class_init)
            gen.append(template_class_init_val.format(long=lk, value=v[2]))
    for (k, v) in spec.items():
        type = 'str' if len(v) < 2  else v[1]
        lk = k if len(v) == 0 or len(v[0]) == 0 else v[0]
        if '->' in lk:
            ccl,a = lk.split('->')
            c, cl = ccl.split(':')
            gen.append(template_nested_property.format(short=k, container=c, attr=a, container_class=cl,type=type))
        else:
            gen.append(template_property.format(short=k, long=lk, type=type))

    if len(gen) == 1:
        gen.append('    pass')
    return gen


if __name__ == "__main__":
    gen = []
    gen.append(
        """
# generated file! see gen_model.py
from typing import List, Set, Dict, Tuple, Optional


        """
    )
    
    for (k, v) in models.items():
        gen.extend(generate(k, v))
        gen.append('')
        gen.append('')

    with open('lti/gen_model.py', 'w') as model:
        model.writelines([l+'\n' for l in gen])
