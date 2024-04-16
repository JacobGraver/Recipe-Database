import json
import os


def update_recipe():
    # Get the name of the recipe to be updated
    name = input(
        print("What is the name of the recipe that you would like to update? ")
    )

    file_name = name + ".json"

    # TODO write search function

    # getting the key for the dict
    recipe = input(print("What part of the recipe would you like to update?"))

    with open(file_name, 'r') as f:
        loaded_dict = json.load(f)

    to_change = input(print('What part of the recipe would you like to change?'))
    
    change = input(print('Please type the changed verion now'))
    
    loaded_dict[to_change] = change

    # load the changed dict into a json string
    json_str = json.dumps(loaded_dict)
    
    # load the json string into a file 
    with open(file_name, 'w') as f:
        loaded_dict = json.load(f)

