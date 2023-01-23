import json
with open("data/json_file.json","r") as f:
    person = json.load(f)


"""for element in person.copy():
    if 'Dolma' in person[element]:
        person.pop(element)"""
for element in members:
    if 'Dawa' in element:
        del members[element]

# writing new_json file after removing item Dolma form from the list
with open("data/new_json.json", "w") as outfile:
    json.dump(person, outfile)