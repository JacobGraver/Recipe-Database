import os
import json


def add_recipe():

    # Gathering the needed information
    recipe_name = input(print('What is the name of the recipe? '))
    prep_time = input(print('What is the prep time for the recipe? '))
    cook_time = input(print('What is the cook time for the recipe? '))
    ingredients = input(print(
        'What are the ingredients? (Please just put a comma between the ingredients) '))
    recipe_steps = input(print(
        'What are the steps to make the recipe? (Please just use seperate sentences for the steps and no need to number them) '))

    # Create the dictionary that all of the inputs are going into
    recipe_temp = {
        "Recipe name": recipe_name,
        "Prep time": prep_time,
        "Cook time": cook_time,
        "Ingredients": ingredients,
        "Steps": recipe_steps
    }

    file_name = str(recipe_temp['Recipe name']) + '.json'
    # Writes the file to a json string
    json_str = json.dumps(recipe_temp)

    # Directory for storing recipes
    directory = 'Recipes'

    # Ensure the directory exists, create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the full path including directory and file name
    file_path = os.path.join(directory, file_name)

    # Serialize dictionary to JSON string
    json_str = json.dumps(recipe)

    # Saves the string to a file
    # It worked the first time but I think the name wont ever change so I need to figure out how to iterate over it
    with open(file_path, 'w') as f:
        f.write(json_str)
