from functools import reduce

class TestResult():

    def __init__(self, name: str, success: bool, required: bool = True,comment: str = ''):
        self.name = name
        self.success = success
        self.comment = comment
        self.required = required


class TestCategory():

    def __init__(self, name: str):
        self.name = name
        self.results = []

    @property
    def success(self) -> bool:
        return reduce(lambda x,y: x and y.success, self.results, True)

