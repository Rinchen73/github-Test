import json
import yaml
import pandas as pd
from yaml.loader import SafeLoader

def json_read_write():
    with open("data/json_file.json","r") as f:
        person = json.load(f)

    #searching for the key and deleting
    for element in person.copy():
        if 'Dolma' in person[element]:
            person.pop(element)

    # writing new_json file after removing item Dolma form from the list
    with open("data/new_json.json", "w") as outfile:
        json.dump(person, outfile)
    return
  
    


def csv_read_write():
    student_list= pd.read_csv('data/stu-list.csv')
    # removing last line for data/stu-list.csv
    student_list= student_list.iloc[:-1]
    # printing modified data/stu-list.csv 
    #print(student_list)
    #saving update info into new csv file
    student_list.to_csv('data/new-stu-list.csv')
    return 

def yaml_read_write():
    # Open the file and load the file
    # Open the file and load the file
    with open('data/yaml_file.yaml') as f:
        members = yaml.load(f, Loader=SafeLoader)

    #deletiing first item from the yaml file
    del members[0]
    
    #updating in the new yaml file
    with open('data/new_yaml.yaml', mode='w') as file:
        yaml.dump(members, file, indent=2)
    return
# calling functions 
json_read_write()
csv_read_write()
yaml_read_write()
