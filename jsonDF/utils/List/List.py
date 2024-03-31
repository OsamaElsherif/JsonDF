import jsonDF

class List:
    def __init__(self, prefix, data):
        self.data = data
        self.prefix = prefix
        self.rows = {}
        self.process()

    def process(self):
        if len(self.data) > 1:
            self.childs(enumerate(self.data))
        elif len(self.data) == 1:
            if type(self.data[0]) == dict:
                self.data = self.data[0]
                return self.childs(list(self.data.keys()))
            else:
                return self.childs(enumerate(self.data))

    def childs(self, keys):
        for key, _ in keys:
            if isinstance(self.data[key], list) or isinstance(self.data[key], dict):
                self.rows[f"{self.prefix}_{key}"] = self.childType(
                    data=self.data[key], prefix=f"{self.prefix}_{key}"
                )
            else:
                self.rows[f"{self.prefix}_{key}"] = self.data[key]

    def childType(self, data, prefix):
        if type(data) == list:
            return List(data=data, prefix=prefix).rows
        elif type(data) == dict:
            return jsonDF.Dict(data=data, prefix=prefix).rows