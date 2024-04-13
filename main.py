import json
import os


def main():
    cmd_prompt()
    

def cmd_prompt():
    choice = input(print(f"What would you like to do?\n(1) Add a new recipe\n(2) View all recipes\n(3) Search for a recipe\n(4) Update a recipe\n(5) Delete a recipe"))

    if choice == '1':
        # TODO write add_recipe function
        add_recipe()

    elif choice == '2':
        # TODO write view_all_recipes function
        print('Yay 2 works')
        
    elif choice == '3':
        # TODO write search_recipe function
        print('Yay 3 works')

    elif choice == '4':
        # TODO write update_recipe function
        print('Yay 4 works')
        
    elif choice == '5':
        # TODO write delete_recipe function
        print('Yay 5 works')
        
    else:
        print('Please make a valid selection')
        cmd_prompt()

def add_recipe():
    
    # Gathering the needed information
    recipe_name = input(print('What is the name of the recipe? '))
    prep_time = input(print('What is the prep time for the recipe? '))
    cook_time = input(print('What is the cook time for the recipe? '))
    ingredients = input(print('What are the ingredients? (Please just put a comma between the ingredients) '))
    recipe_steps = input(print('What are the steps to make the recipe? (Please just use seperate sentences for the steps and no need to number them) '))
    
    # Create the dictionary that all of the inputs are going into
    recipe = {
        "Recipe name": recipe_name,
        "Prep time": prep_time,
        "Cook time": cook_time,
        "Ingredients": ingredients,
        "Steps": recipe_steps
        
    }
    
    file_name = str(recipe['Recipe name']) + '.json'
    # Writes the file to a json string
    json_str = json.dumps(recipe)
    
    # Directory for storing recipes
    directory = 'Recipes'

    # Ensure the directory exists, create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Construct the full path including directory and file name
    file_path = os.path.join(directory, file_name)

    # Serialize dictionary to JSON string
    json_str = json.dumps(my_dict)
    
    # Saves the string to a file
    # It worked the first time but I think the name wont ever change so I need to figure out how to iterate over it
    with open(file_path, 'w') as f:
        f.write(json_str)
        
    # # Reads the json file back into python as a dict again
    # with open('something.json', 'r') as f:
    #     loaded_dict = json.load(f)
    
    # test
    # print(loaded_dict)
    
    # TODO make the steps that take the dictionary and parse it and save it as a json file
    # I dont think that I am going to have to parse it because it is very simple to take the info as is
    


main()
