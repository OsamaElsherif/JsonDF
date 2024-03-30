import sys 

sys.path.append('.')

from jsonDF.utils.Json.DeSesrializer.DeSearializer import DeSearializer


Human = DeSearializer("Human.jdf", True).DeSearilize()

h = Human("Kazagashi", "21")
h.job("Software Developer")
print(h.whoami())