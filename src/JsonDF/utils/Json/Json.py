class Json:
    def __init__(self, name, json={}):
        self.json = json
        self.json_name = name
    
    def objectiy(self):
        keys = self.json.keys()
        for key in keys:
            value = self.value(self.json[key])
            self.__setattr__(key, value)
        return self
    
    def insert(self, name, value):
        self.__setattr__(name, value)
        return self
    
    def delete(self, name):
        del self.__dict__[name]
        return self
    
    def dump(self, name):
        valueType = type(self.__getattribute__(name))
        if valueType == Json:
            self.__setattr__(name, Json('0', {}))
        elif valueType == list:
            self.__setattr__(name, [])
        elif valueType == dict:
            self.__setattr__(name, {})
        elif valueType == str:
            self.__setattr__(name, '')
        else:
            self.__setattr__(name, 0)
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
            if attr.startswith('__') or callable(attr) or attr == 'json' or attr == 'json_name':
                continue
            attrs[attr] = getattr(self, attr)
        return attrs

    def __repr__(self):
        return self.show().__str__()