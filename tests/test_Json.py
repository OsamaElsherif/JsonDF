import unittest
from FiJson.utils.Json.Json import Json


class TestJson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dict = {"name": "python"}
        cls.obj = Json(name="foo", json=cls.temp_dict)

    def test_init(self):
        self.assertEqual(self.obj.json, self.temp_dict)
        self.assertEqual(self.obj.json_name, "foo")
        self.assertEqual(self.obj.__depth__, 0)

    def test_objectify(self):
        self.assertIsInstance(self.obj.objectiy(), Json)

    def test_find(self):
        pass

    def test_insert(self):
        key = "foo"
        value = "bar"

        self.assertIsInstance(self.obj.insert(key, value), Json)

        self.assertEqual(self.obj.find(key), value)

    def test_delete(self):
        print("=" * 50)
        print(self.obj.find("name"))
        print("=" * 50)

    @classmethod
    def tearDownClass(cls):
        pass
