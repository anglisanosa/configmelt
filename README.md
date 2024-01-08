# configmelt

## Introduction
The ConfigMeld package simplifies configuration handling by providing a class to manage JSON or YAML configurations. This class allows for easy loading, accessing, and manipulation of configuration attributes.

## Installation
To install configmelt, simply use pip:

```bash
pip install configmelt

```
## Features:
- **Loading Configurations**: Load configurations from JSON or YAML files.
- **Accessing Configurations**: Access configuration attributes as object properties.
- **Flexible Representation**: Manage configurations in an object-oriented manner.
- **Environmental Integration**: Easily convert configurations to environment variables.
- **Schema Generation**: Generate JSON schema based on existing configurations.

## Usage
1. Initializing ConfigMeld:

``` python
from configmeld import ConfigMeld

# Initialize ConfigMeld with attributes
config = ConfigMeld(foo='bar', nested={'key': 'value'})

# Access configuration attributes
print(config.foo)  # Output: 'bar'

```

2. Loading Configurations from Files:

```python
# Load configurations from a JSON/YAML file
path_to_config = 'path/to/config.json'
loaded_config = ConfigMeld.load_config_from_file(path_to_config)

# Access loaded configurations
print(loaded_config.attribute_name)

```

3. schema Generation:

```python
# Generate JSON schema based on existing configurations
schema = loaded_config.generate_schema()
print(schema)
```


## Documentation
The Sphinx-generated documentation for configmelt can be found [here](https://anglisanosa.github.io/configmelt/).

## Contribution
Feel free to contribute by submitting issues [here](https://github.com/anglisanosa/configmelt/issues).