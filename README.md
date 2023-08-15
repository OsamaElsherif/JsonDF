# JsonDF [Json parser for DataFrane usage]

This package is a package for converting nested Json/Dictionaries/Lists for DataFrame usage

## Download

for latest release
```
pip install JsonDF==1.0.3
```
## Normal Usage

and to use it : 

```python
from JsonDf.Data import Data

data = Data(prefix="your_prefered_prefix_default_is_root", data=YourJson)

data.childs() #for processing the childs of the Json/Dict/List
print(data.rows) #organized dictionary with the data !! Not for DataFrame usage
data.flatten() #for flattening the result for DataFram usage
print(data.rows_flatten) #flatten the data for DataFrame usage
```

## Json type usage

In Json type you have the ability to parse Json/Dict in the sameway it parsed in JQuery, in addition to the ability to make objects automatically from json/dict

to use it : 

```python
from Json.utils.Json import Json

some_json = {
  'keys' : {
    "another_key": "some_value",  
    },
}

json = Json(json=some_json, name=any_name)
json.objectify()
print(json)
print(json.keys)
print(json.keys.another_key)
```

feel free to contribute in this project.

cheers.
