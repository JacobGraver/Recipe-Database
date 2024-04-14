import json
import os

def update_recipe():
    # Get the name of the recipe to be updated
    name = input(print('What is the name of the recipe that you would like to update? '))
    
    try:
        # Search and make sure the recipe exists
        # Might not work and might need to be updated 
        # FIXME
        os.path.isfile('/home/myth/Git/Recipe-Database/Recipes')
        
    except Exception as e:
        print(f'Error: {e}')
        
    # Get the part of the recipe that needs updated
    change = input(print('What part of the recipe would you like to update?'))
    