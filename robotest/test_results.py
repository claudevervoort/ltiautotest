from functools import reduce

class TestResult():

    def __init__(self, name: str, success: bool, required: bool = True,comment: str = '', comment_pre: str = '', link: str = '', dom_id: str =''):
        self.name = name
        self.success = success
        self.comment = comment
        self.comment_pre = comment_pre
        self.required = required
        self.link = link
        self.dom_id = dom_id


class TestCategory():

    def __init__(self, name: str):
        self.name = name
        self.results = []

    @property
    def success(self) -> bool:
        return all(map(lambda x: x.success or not x.required, self.results))

