
class LTIResourceLink(dict):

    def get_or_create_lineitem(self):
        if self.get('lineItem'):
            return self['lineItem']
        self['lineItem'] = {
            'scoreMaximum': 100
        }
        return self['lineItem']

    def __max_points(self) -> float:
        if self.get('lineItem'):
            return self['lineItem']['scoreMaximum']
        return None

    def __set_max_points(self, points: float):
        self.get_or_create_lineitem()['scoreMaximum'] = points

    def __getattr__(self, key):
        if (key=='max_points'):
            return self.__max_points() 
        return self.__getitem__(key)

    def __setattr__(self, key, val):
        if (key=='max_points'):
            self.__set_max_points(val) 
        self.__setitem__(key, val)
