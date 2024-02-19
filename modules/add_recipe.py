import sqlite3

def add_recipe():
    
    conn = sqlite3.connect('recipes.db')

    #################################################################
    ######################### RECIPE NAME ###########################
    #################################################################
    
    # Get the name of the recipe and create a table that is named after the recipe and has the recipe name in the table
    
    recipe_name = input(f"What is the name of the recipe?\n")
    
    conn.execute("CREATE TABLE *(RecipeName, PrepTime, CookTime, Ingredients, Instructions)", recipe_name)
    conn.execute("INSERT INTO *(RecipeName) VALUES(recipe_name)")

    #################################################################
    ########################## Prep Time ############################
    #################################################################

    # Get the prep time and put it into the table 
    prep_time = input(f"How long does the recipe take to prep?\n")
    conn.execute("INSERT INTO * (PrepTime) VALUES(*)", recipe_name, prep_time)

    #################################################################
    ########################## Cook Time ############################
    #################################################################

    cook_time = input(f"How long does the recipe take to cook?\n")
    conn.execute("INSERT INTO * (CookTime) VALUES(*)", recipe_name, cook_time)
    
    #################################################################
    ######################### Ingredients ###########################
    #################################################################

    ingredients = input(f"What is the first ingredient?\n")
    conn.execute("INSERT INTO * (Ingredients) VALUES(*)", recipe_name, ingredients)

    # Decision loop for adding more ingredients
    while True:
        choice = input(f"Would you like to add another ingredient? ('y' or 'n')\n")
        if choice == 'n':
            break

        elif choice == 'y':
            ingredient = input(f"What is the ingredient?\n")
            conn.execute("INSERT INTO * (Ingredients) VALUES(*)", recipe_name, ingredient)
            
        else:
            print(f"Please enter a valid selection\n")

    #################################################################
    ######################### Instructions ##########################
    #################################################################

    # Adding the instructions to the db 
    # Each step (*should) be in its own cell in the column so that is how they will be displayed
    step_1 = input(f"What is the first step?\n")
    conn.execute("INSERT INTO * (Instructions) VALUES (*)", recipe_name, step_1)

    # Reseting the value for choice so it cant cause issues
    choice = ' '

    # Decision loop for the steps of the recipe 
    while True:
        choice = input(f"Would you like to add another step?('y' or 'n')\n")
        if choice == 'n':
            break

        elif choice == 'y':
            next_step = input(f"What is the next step?\n")
            conn.execute("INSERT INTO * (Instructions) VALUES (*)", recipe_name, next_step)
        
        else:
            print(f"Please enter a valid selection\n")


add_recipe()