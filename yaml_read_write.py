from yaml.loader import SafeLoader
import yaml

def main(paths):
    index =1
    for path in paths:
        yaml_data=read_yaml(path)
        updated_data=update_yaml(yaml_data)
        save_yaml(updated_data,index)
        
        index =index +1
def read_yaml(path):
    with open(path) as f:
        yaml_file = yaml.load(f, Loader=SafeLoader)
        return yaml_file
def update_yaml(yaml_file):
    del yaml_file[0]
    return yaml_file    
def save_yaml(updated_data,index):
   with open(f'updated_yaml_files/updated{index}.yaml', mode='w') as file:
    yaml.dump(updated_data, file, indent=2) 


if __name__=="__main__":
    
    paths =["./yaml_files/yaml_file1.yaml",
            "./yaml_files/yaml_file2.yaml",
            "./yaml_files/yaml_file3.yaml",
            "./yaml_files/yaml_file4.yaml",
            "./yaml_files/yaml_file5.yaml",
            "./yaml_files/yaml_file6.yaml",
            "./yaml_files/yaml_file7.yaml",
            "./yaml_files/yaml_file8.yaml",
            "./yaml_files/yaml_file9.yaml",
            "./yaml_files/yaml_file10.yaml",
           ]
    main(paths)