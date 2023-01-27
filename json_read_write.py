import json

def main(paths):
    index = 1
    for path in paths:
        data = read_json(path)
        updated_data =update(data)
        save_json(updated_data,index)
        index = index + 1

def read_json(path):
    file = open(path)
    json_data = json.load(file)
    return json_data

def update(update_data):
    key_name=[]
    for key, element in update_data.items():
        key_name.append(key)

    if("Dolma" in key_name):
        update_data.pop("Dolma")
    return update_data
    

def save_json(data,index):
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
    