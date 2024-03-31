from FiJson.utils.Json.Json import Json


temp_dict = {"name": "python"}
obj = Json(name="foo", json=temp_dict)

print(obj.delete("name"))
print(type(obj.find("name")))
