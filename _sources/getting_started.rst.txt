Getting started
===============

Usage
-----

1. Initializing ConfigMeld::

    from configmeld import ConfigMeld

    # Initialize ConfigMeld with attributes
    config = ConfigMeld(foo='bar', nested={'key': 'value'})

    # Access configuration attributes
    print(config.foo)  # Output: 'bar'

2. Loading Configurations from Files::

    # Load configurations from a JSON/YAML file
    path_to_config = 'path/to/config.json'
    loaded_config = ConfigMeld.load_config_from_file(path_to_config)

    # Access loaded configurations
    print(loaded_config.attribute_name)

3. Schema Generation::

    # Generate JSON schema based on existing configurations
    schema = loaded_config.generate_schema()
    print(schema)