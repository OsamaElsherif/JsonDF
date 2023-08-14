### JsonDF [Json parser for DataFrane usage]

This package is a package for converting nested Json/Dictionaries/Lists for DataFrame usage

for latest release
```
pip insyall JsonDF==1.0.3
```

and to use it : 

```python
import JsonDf.Data as Data

data = Data(prefix="your_prefered_prefix_default_is_root", data=YourJson)

data.childs() #for processing the childs of the Json/Dict/List
print(data.rows) #organized dictionary with the data !! Not for DataFrame usage
data.flatten() #for flattening the result for DataFram usage
print(data.rows_flatten) #flatten the data for DataFrame usage
```

feel free to contribute in this project.

cheers.
