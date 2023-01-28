from yaml.loader import SafeLoader
import yaml

def read_yaml(paths):
    with open(paths) as file:
        yaml_data = yaml.full_load(file, Loader=SafeLoader)
    return yaml_data
    
if __name__== "__main__":
    paths=["./yamal_files/yaml_file1.yaml"]
    yaml_file =read_yaml(paths)
    