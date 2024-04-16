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

    with open(file_name) as f:
        loaded_dict = json.load(f)
