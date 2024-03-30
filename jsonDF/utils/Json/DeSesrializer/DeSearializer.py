from ..Json import Json
import gzip
import base64
import ast

class DeSearializer:
    def __init__(self, searilized_object:Json|str, from_file=False) -> None:
        self.__from_file = from_file
        if from_file:
            self.searilized_object = searilized_object
        else:
            self.searilized_object      = searilized_object.objectiy()
            self.__name                 = self.searilized_object.name
            self.__params               = self.searilized_object.params
    
    def __interpet(self):
        if self.__from_file:
            self.searilized_object  = Json("BaseObject", self.__load()).objectiy()
            self.__name             = self.searilized_object.name
            self.__params           = self.searilized_object.params
        
        __num_params = len(self.__params.show())
        __inhertance = "" if 0 == __num_params else f"({self.__params})"
        self.__create_class(__inhertance)
        self.__methods()

        return self.__object
    
    def __load(self):
        __obj = open(f"{self.searilized_object}", "rb").read()
        __obj = gzip.decompress(__obj)
        __obj = base64.b64decode(__obj)
        return ast.literal_eval(__obj.decode())

    
    def __create_class(self, __inhertance) -> object:
        if __inhertance != "":
            self.__object =  type(f"{self.__name}", (eval(f"{__inhertance}", object)), {})
        else:
            self.__object =  type(f"{self.__name}", (object,), {})

    
    def __methods(self) -> None:
        for __method_name in self.searilized_object.methods.show():
            __code_text = """"""
            __code_text_lines = self.searilized_object.methods.find(__method_name).find(__method_name).code.split('\n')
            __code_text_lines = [ line[4:] for line in __code_text_lines]
            __code_text += "\n".join(__code_text_lines)

            exec(compile(__code_text, filename=f"{__method_name}.py", mode="exec"))
            __method_name_ = __method_name.split('.')[-1]
            setattr(self.__object, f"{__method_name_}", eval(f"{__method_name_}"))

    
    def DeSearilize(self) -> object:
        return self.__interpet()