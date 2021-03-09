from model import models

template_enum = """
class {name}(Enum):

"""

template_class_val = """
    {name} = '{value}'
"""

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
        val = self.get('{long}')
        if issubclass({type}, Enum):
            return {type}(val)
        if (isinstance(val, dict) and not isinstance(val, {type})):
            typed_val = {type}( **val )
            self['{long}'] = typed_val
            return typed_val
        return val


    @{short}.setter
    def {short}(self, value: {type}):
        if isinstance(value, Enum):
            self['{long}'] = value.value
        else:
            self['{long}'] = value
"""

template_datetime_property = """
    @property
    def {short}(self) -> datetime:
        val = self.get('{long}')
        if (val):
            return datetime.fromisoformat(val)
        return None

    @{short}.setter
    def {short}(self, value: datetime):
        self['{long}'] = value.isoformat()
"""

template_bool_property = """
    @property
    def {short}(self) -> bool:
        val = self.get('{long}')
        if (val):
            if type(val) is bool:
                return val
            # Moodle error encoded a string
            if type(val) is str:
                return val.lower() == 'true'
            return False
        return None

    @{short}.setter
    def {short}(self, value: bool):
        self['{long}'] = value
"""

template_dict_property = """
    @property
    def {short}(self) -> {type}:
        if not '{long}' in self:
            self['{long}'] = {{}}
        return self.get('{long}')

    @{short}.setter
    def {short}(self, value: {type}):
        self['{long}'] = value
"""

template_list_property = """
    @property
    def {short}(self) -> {type}:
        if not '{long}' in self:
            self['{long}'] = []
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

def generate_enum(name: str, spec: tuple):
    gen = []
    gen.append(template_enum.format(name=name))
    for item in spec:
        gen.append(template_class_val.format(name=item.upper(), value=item))
    return gen


def generate_class(name: str, spec: dict):
    gen = []
    gen.append(template_class.format(name=name))
    init = False
    for (k, v) in spec.items():
        if k=='cls_const':
            for (kk,vv) in v.items():
                gen.append(template_class_val.format(name=kk, value=vv))
        elif len(v) == 3:
            lk = k if len(v) == 0 or len(v[0]) == 0 else v[0]
            if not init:
                gen.append(template_class_init)
                init = True
            gen.append(template_class_init_val.format(long=lk, value=v[2]))
    items = (item for item in spec.items() if isinstance(item[1], list) )
    for (k, v) in items:
        type = 'str' if len(v) < 2 else v[1]
        lk = k if len(v) == 0 or len(v[0]) == 0 else v[0]
        if '->' in lk:
            ccl, a = lk.split('->')
            c, cl = ccl.split(':')
            gen.append(template_nested_property.format(
                short=k, container=c, attr=a, container_class=cl, type=type))
        elif type.startswith('List'):
            gen.append(template_list_property.format(
                short=k, long=lk, type=type))
        elif type.startswith('Dict'):
            gen.append(template_dict_property.format(
                short=k, long=lk, type=type))
        elif type == 'datetime':
            gen.append(template_datetime_property.format(
                short=k, long=lk))
        elif type == 'bool':
            gen.append(template_bool_property.format(
                short=k, long=lk))
        else:
            gen.append(template_property.format(short=k, long=lk, type=type))

    if len(gen) == 1:
        gen.append('    pass')
    return gen


if __name__ == "__main__":
    gen = []
    gen.append(
        """
# generated file! see codegen.py
from typing import List, Set, Dict, Tuple, Optional
from enum import Enum
from datetime import datetime

        """

    )

    for (k, v) in models.items():
        if isinstance(v, dict):
            gen.extend(generate_class(k, v))
        else:
            gen.extend(generate_enum(k, v))
        gen.append('')
        gen.append('')

    with open('lti/gen_model.py', 'w') as model:
        model.writelines([l+'\n' for l in gen])
