import json

def main(paths):
    """Main Function to call the other values

    Args:
        paths (list): all the 10 files' path in list
    """    
    index = 1
    for path in paths:
        data = read_json(path)
        updated_data =update(data)
        save_json(updated_data,index)
        index = index + 1

def read_json(path):
    """to read the json file 

    Args:
        path (str): path of json file in string

    Returns:
        Dict: Dictionary ( contains key values pairs)
    """    
    file = open(path)
    json_data = json.load(file)
   
    return json_data

def update(update_data):
    """to do change in dictionary 

    Args:
        update_data (dict): key value paired data, 

    Returns:
        dict: dictionary -> returning updated dict
    """    
    key_name=[]
    for key, element in update_data.items():
        key_name.append(key)

    if("Dolma" in key_name):
        update_data.pop("Dolma")
    return update_data
    

def save_json(data,index):
    """write the updated dictionary data to a new json file

    Args:
        data (dict): updated key value pair
        index (int):unumber fro range (1-10)
    """    
    with open(f"./updated_json/updated{index}.json", "w") as update_file:
        json.dump(data,update_file)

if __name__ == "__main__":
    paths=["./json_files/json_file1.json",
    "./json_files/json_file2.json",
    "./json_files/json_file3.json",
    "./json_files/json_file4.json",
    "./json_files/json_file5.json",
    "./json_files/json_file6.json",
    "./json_files/json_file8.json",
    "./json_files/json_file9.json",
    "./json_files/json_file10.json",
    ]
    main(paths)
    