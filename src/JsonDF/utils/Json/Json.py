class Json:
    def __init__(self, name, json={}):
        self.json = json
        self.name = name
    
    def objectiy(self):
        keys = self.json.keys()
        for key in keys:
            value = self.value(self.json[key])
            self.__setattr__(key, value)
        return self
    
    def insert(self, name, value):
        self.__setattr__(name, value)
        return self
    
    def value(self, value):
        if type(value) == dict or type(value) == list:
            if type(value) == list:
                return [self.process(value)]
            else:
                return Json(0, value).objectiy()
        else:
            return value

    def process(self, value):
        if value == None: return []
        for val in value:
            if type(val) == dict:
                return Json(0, val).objectiy()
    
    def show(self):
        attrs = {}
        for attr in vars(self):
            if attr.startswith('__') or callable(attr) or attr == 'json':
                continue
            attrs[attr] = getattr(self, attr)
            return attrs

    def __repr__(self):
        return self.show().__str__()