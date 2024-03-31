class Json:
	"""
    Provides an object-oriented interface for working with JSON data.

    This class converts JSON dictionaries into objects with attributes corresponding to the JSON keys,
    allowing for easy access and manipulation of JSON data using dot notation. It handles nested
    structures, supports data insertion and deletion, and offers search functionality.
    """

	def __init__(self, name, json={}, depth=0) -> None:
		"""
		The Json class provides a structured and object-oriented way to interact with JSON data. 
		It takes a JSON dictionary (or an empty dictionary by default) and transforms it into an object 
		with attributes corresponding to the JSON keys. This allows you to access and manipulate 
		JSON data using dot notation, similar to working with regular Python objects.

		Args:
			name (_type_): Prefix of Json
			json (dict, optional): Custom Dictionay. Defaults to {}.
			depth (int, optional): Depth of the Json/Dict. Defaults to 0.
		
		Returns:
			None
		"""

		self.json = json
		self.json_name = name
		self.__depth__ = depth
		self.__total_depth__ = 0
		self.__depth_in__ = []

	def objectiy(self):
		"""
		Converts the JSON dictionary into an object with attributes corresponding to the JSON keys.

		This method iterates through the dictionary, converting values into appropriate Python objects
		and creating attributes on the current Json object for each key-value pair. Nested dictionaries
		and lists are handled recursively, creating new Json objects for nested structures.

		Returns:
			Json: The current Json object (self) for method chaining.
		"""
		keys = self.json.keys()
		for key in keys:
			value = self.__value(self.json[key], key)
			self.__setattr__(key, value)
		return self

	def insert(self, name, value):
		"""
		Inserts a new key-value pair into the Json object.

		Args:
			name (str): The name of the key to create.
			value (any): The value to assign to the key.

		Returns:
			Json: The current Json object (self) for method chaining.
		"""
		
		self.__setattr__(name, value)
		return self

	def delete(self, name):
		"""
		Deletes an attribute from the Json object.

		Args:
			name (str): The name of the key to remove.

		Returns:
			Json: The current Json object (self) for method chaining.
		"""

		del self.__dict__[name]
		return self

	def dump(self, name):
		"""
		Initializes an attribute with a default value based on its type.

		This method sets the attribute to an empty dictionary, list, string, or 0 depending on
		whether it is a Json object, list, string, or other type, respectively.

		Args:
			name (str): The name of the key to initialize.

		Returns:
			Json: The current Json object (self) for method chaining.
		"""

		valueType = type(self.__getattribute__(name))
		if valueType == Json:
			self.__total_depth__ += 1
			self.__depth_in__.append(self.name)
			self.__setattr__(name, Json(0, {}, self.__depth__ + 1))
		elif valueType == list:
			self.__setattr__(name, [])
		elif valueType == dict:
			self.__setattr__(name, {})
		elif valueType == str:
			self.__setattr__(name, "")
		else:
			self.__setattr__(name, 0)
		return self

	def find(self, name, report=False):
		"""
		Searches for a key within the Json object.

		Args:
			name (str): The name of the key to find.
			report (bool, optional): If True, returns a tuple with the value and a success flag.
									Defaults to False, returning only the value or an error message.

		Returns:
			any or tuple: The value of the attribute if found, or an error message if not found.
						If report is True, returns a tuple (value, success_flag).
		"""

		try:
			value = self.__getattribute__(name)
			return (value, True) if report else value
		except:
			return (
				(
					(
						self.__depth__,
						f"No results for {name} in {self.json_name} at depth {self.__depth__}",
					),
					False,
				)
				if report
				else f"No results for {name} in {self.json_name} at depth {self.__depth__}"
			)

	def find_all(self, name, reports=True, query=[]):
		"""
		Recursively searches for all occurrences of a key within the Json object and its nested structures.

		Args:
			name (str): The name of the key to find.
			reports (bool, optional): If True, prints messages for unsuccessful searches. Defaults to True.
			query (list, optional): A dictionary to store found attributes and their values. Defaults to {}.

		Returns:
			tuple: A tuple containing the updated query dictionary and a success flag.
		"""

		query = query
		result = self.find(name, True)
		if result[1]:
			query.append({(self.__depth__, name, self.json_name): self.find(name, True)[0]})
		else:
			if reports:
				print(result[0][1])

		if self.depth_check(self):
			for depth_point in self.__depth_in__:
				if type(self.__getattribute__(depth_point)) == list:
					for element in self.__getattribute__(depth_point):
						element.find_all(name, reports, query)
				else:
					self.__getattribute__(depth_point).find_all(name, reports, query)

		return (query, True)

	def depth_check(self, json: object):
		"""
		Checks if the provided Json object has nested structures.

		Args:
			json (Json): The Json object to check.

		Returns:
			bool: True if the object has nested structures, False otherwise.
		"""

		if json.__total_depth__ > 0:
			return True
		return False

	def __value(self, value, key):
		"""
		Converts a JSON value into an appropriate Python object.

		This method handles nested dictionaries and lists by creating new Json objects recursively.

		Args:
			value (any): The JSON value to convert.
			key (str): The key associated with the value.

		Returns:
			any: The converted Python object.
		"""

		if isinstance(value, dict) or isinstance(value, list):
			if isinstance(value, list):
				return self.process(value, key)
			else:
				self.__total_depth__ += 1
				self.__depth_in__.append(key)
				return Json(
					f"{self.json_name}.{key}", value, self.__depth__ + 1
				).objectiy()
		else:
			return value

	def process(self, value, key):
		"""
		Processes a JSON list, converting nested dictionaries into Json objects.

		Args:
			value (list): The JSON list to process.
			key (str): The key associated with the list.

		Returns:
			list: The processed list with nested dictionaries converted to Json objects.
		"""

		__list = []
		if value is None:
			return []
		for val in value:
			if isinstance(val, dict):
				self.__total_depth__ += 1
				if self.__depth_in__.count(key) < 1:
					self.__depth_in__.append(key)
				__list.append(
					Json(f"{self.json_name}.{key}", val, self.__depth__ + 1).objectiy()
				)
				continue

			__list.append(val)
		return __list

	def show(self):
		"""
		Returns a dictionary representation of the Json object's attributes, excluding internal attributes.

		Returns:
			dict: A dictionary containing the object's attributes and their values.
		"""

		attrs = {}
		for attr in vars(self):
			if (
				attr.startswith("__")
				or callable(attr)
				or attr == "json"
				or attr == "json_name"
			):
				continue
			attrs[attr] = getattr(self, attr)
		return attrs

	def __repr__(self):
		"""
		Returns a string representation of the Json object, displaying its attributes and values.

		Returns:
			str: A string representation of the object.
		"""

		return self.show().__str__()