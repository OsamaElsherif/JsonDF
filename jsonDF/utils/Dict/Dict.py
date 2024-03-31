import jsonDF

class Dict:
    def __init__(self, data, prefix):
        self.data = data
        self.prefix = prefix
        self.rows = {}
        self.process()

    def process(self) -> None:
        if len(self.data.keys()) >= 1:
            self.childs(list(self.data.keys()))

    def childs(self, keys) -> None:
        for key in keys:
            if isinstance(self.data[key], list) or isinstance(self.data[key], dict):
                self.rows[f"{self.prefix}_{key}"] = self.childType(
                    data=self.data[key], prefix=f"{self.prefix}_{key}"
                )
            else:
                self.rows[f"{self.prefix}_{key}"] = self.data[key]

    def childType(self, data, prefix):
        if isinstance(data, list):
            return jsonDF.List(data=data, prefix=prefix).rows
        elif isinstance(data, dict):
            return Dict(data=data, prefix=prefix).rows
