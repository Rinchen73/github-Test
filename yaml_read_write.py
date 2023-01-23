import pandas as pd
from yaml.loader import SafeLoader
import yaml

# Open the file and load the file
with open('data/yaml_file.yaml') as f:
    members = yaml.load(f, Loader=SafeLoader)

#deletiing first item from the yaml file
del members[0]

#updating in the new yaml file
with open('data/new_yaml.yaml', mode='w') as file:
    yaml.dump(members, file, indent=2)