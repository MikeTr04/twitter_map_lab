"""LAB 2_2"""


import json


hierarchy = []
with open('kved.json', 'r', encoding="utf8") as file1:
    data = json.load(file1)
while True:
    obj = data
    for i in hierarchy:
        obj = obj[i]
    print("You are analysing a", type(obj))
    print(f"The object has {len(obj)} elements.")
    if type(obj) is dict:
        direction = input("Do you want to choose a key, view contents, or go back? Key/Back/Contents: ")
        if direction == 'Key':
            key = input("Choose a key: ")
            if key not in obj.keys():
                print("Invalid key!")
                continue
            if not isinstance(obj[key], dict) and not isinstance(obj[key], list) and not isinstance(obj[key], tuple):
                print("YOOOOOOOO")
                print(obj[key])
            else:
                hierarchy.append(key)
                continue
        elif direction == "Back":
            if len(hierarchy) == 0:
                print("You cannot go any further back!")
            else:
                hierarchy = hierarchy[:-1]
        elif direction == "Contents":
            print('These are the keys in the json file:')
            print([*obj])
    else:
        direction = input("Do you want to output the contents, just choose the "
                          "index, or go back? Index/Contents/Back: ")
        if direction == "Index":
            ind = input("Input the integer index from 0: ")
            hierarchy.append(int(ind))
        elif direction == "Back":
            if len(hierarchy) == 0:
                print("You cannot go any further back!")
            else:
                hierarchy = hierarchy[:-1]
        elif direction == "Contents":
            print(obj)
