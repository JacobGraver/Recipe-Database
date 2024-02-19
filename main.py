import sqlite3

# Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect('recipes.db')

# Your table creation SQL statements here
table_creation_sql = """
CREATE TABLE Recipes (
    RecipeID INTEGER PRIMARY KEY,
    RecipeName TEXT NOT NULL,
    PrepTime INTEGER,
    CookTime INTEGER,
    Ingredients TEXT,
    Instructions TEXT
);
-- Create other tables as needed
"""

def main():
	cli_prompt()

# conn.execute(table_creation_sql)

def cli_prompt():
	# TODO Make a while loop so that this is the main screen and you stay on it until you pick a valid selection
	try:
		choice = input(f"What would you like to do? (Press Enter when you are done typing)\n1. Select a recipe\n2. Add a recipe\n3. Change a recipe\n4. Delete a recipe\n5. Exit\n")

		# TODO add the if statements for selections after the functions are made
		while True:
			if (choice == '1'):
				print("thank for choose 1")
			elif(choice == '2'):
				# print("thank for choose 2")
				add_recipe()
			elif(choice == '3'):
				print("thank for choose 3")
			elif(choice == '4'):
				print("thank for choose 4")
			elif(choice == '5'):
				print("Thank you for using my program")
				break
			else:
				print(choice + " is not a valid selection.")

	except Exception as e:
		print(f"Error: {e}")
		

def add_recipe():

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
	while choice != 'no':
		choice = ' '
		choice = input(f"Would you like to add another ingredient? ('yes' or 'no')\n")

		ingredient = input(f"What is the ingredient?\n")
		conn.execute("INSERT INTO * (Ingredients) VALUES(*)", recipe_name, ingredient)

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
	while choice != 'no':
		choice = ' '
		choice = input(f"Would you like to add another step?('yes' or 'no')\n")

		next_step = input(f"What is the next step?\n")
		conn.execute("INSERT INTO * (Instructions) VALUES (*)", recipe_name, next_step)



main()

