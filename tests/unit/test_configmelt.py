import unittest
import os
from configmelt import ConfigMeld


class TestConfigMeld(unittest.TestCase):
    def test_load_config_from_file(self):
        # Test loading configuration from a JSON file
        json_file = 'path/to/config.json'
        cm_json = ConfigMeld.load_config_from_file(json_file)
        self.assertIsInstance(cm_json, ConfigMeld)

        # Test loading configuration from a YAML file
        yaml_file = 'path/to/config.yaml'
        cm_yaml = ConfigMeld.load_config_from_file(yaml_file)
        self.assertIsInstance(cm_yaml, ConfigMeld)

    def test_load_config_as_environ_vars(self):
        cm = ConfigMeld(a=1, b=2, c={'x': 3, 'y': 4})
        cm.load_config_as_environ_vars()
        self.assertEqual(os.environ['a'], '1')
        self.assertEqual(os.environ['b'], '2')
        self.assertEqual(os.environ['c'], "{'x': 3, 'y': 4}")

    def test_load_config_as_string(self):
        cm = ConfigMeld(a=1, b=2, c={'x': 3, 'y': 4})
        config_str = cm.load_config_as_string()
        self.assertIsInstance(config_str, str)
        self.assertIn('a: 1', config_str)
        self.assertIn('b: 2', config_str)
        self.assertIn('c:\n  x: 3\n  y: 4', config_str)

    def test_generate_schema(self):
        cm = ConfigMeld(a=1, b=2, c={'x': 3, 'y': 4})
        schema = cm.generate_schema()
        self.assertIsInstance(schema, dict)
        self.assertIn('a', schema)
        self.assertIn('b', schema)
        self.assertIn('c', schema)
        self.assertEqual(schema['a'], {'type': 'int'})
        self.assertEqual(schema['b'], {'type': 'int'})
        self.assertEqual(schema['c'], {'type': 'object', 'properties': {'x': {'type': 'int'}, 'y': {'type': 'int'}}})


# if __name__ == '__main__':
#     unittest.main()