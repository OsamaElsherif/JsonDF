import sys 

sys.path.append('.')

from jsonDF.utils.Json.Searializer.Serializer import Serializer
 
class Human:
    def __init__(self, name, age) -> None:
        self.name   = name
        self.age    = age
    
    def job(self, title) -> None:
        self.title = title

    def whoami(self) -> str:
        return f"I am {self.name}, {self.age} yrs old, and I am {self.title}"


Serializer(Human).save()