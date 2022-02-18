"""LAB 2_2"""


import json


def analyze():
    """
    Function to analyze the json file by the given path.
    The file is loaded with json.load().
    The function identifies the type of the current data. If it is tuple, list or dict,
    It is proposed to either look through the contents/keys, choose a key or an index to
    move to, or go back. If it is impossible to go back, the messsage with error is reported
    and there is no move.
    To realize the system of moves, the path of indexes or keys is saved in the
    hierarchy list. To access the current position in json file, the indexes are retrieved
    and joined.
    """
    path = input("Enter path to file: ")
    hierarchy = []
    with open(path, 'r', encoding="utf8") as file1:
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


if __name__ == "__main__":
    analyze()
