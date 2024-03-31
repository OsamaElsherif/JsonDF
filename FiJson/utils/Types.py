from abc import abstractmethod


class BaseType:
    def __init__(self, data, prefix) -> None:
        self.data = data
        self.prefix = prefix
        self.rows = {}
        self.process()

    @abstractmethod
    def process(self):
        pass

    def childs(self, keys):
        for key in keys:
            if not isinstance(self.data[key], (list, dict)):
                self.rows[f"{self.prefix}_{key}"] = self.data[key]
                continue

            self.rows[f"{self.prefix}_{key}"] = self.childType(
                data=self.data[key], prefix=f"{self.prefix}_{key}"
            )

    def childType(self, data, prefix):
        if isinstance(data, list):
            return self.create_list(data=data, prefix=prefix).rows
        elif isinstance(data, dict):
            return self.create_dict(data=data, prefix=prefix).rows

    def create_dict(self, data, prefix):
        return Dict(data=data, prefix=prefix)

    def create_list(self, data, prefix):
        return List(data=data, prefix=prefix)


class Dict(BaseType):
    def __init__(self, data, prefix) -> None:
        super().__init__(data=data, prefix=prefix)

    def process(self) -> None:
        if len(self.data.keys()) >= 1:
            self.childs(list(self.data.keys()))


class List(BaseType):
    def __init__(self, data, prefix) -> None:
        super().__init__(data=data, prefix=prefix)

    def process(self) -> None:
        if len(self.data) > 1:
            self.childs(range(len(self.data)))

        elif len(self.data) == 1:
            if isinstance(self.data[0], dict):
                self.data = self.data[0]
                return self.childs(list(self.data.keys()))
            else:
                return self.childs(range(len(self.data)))
