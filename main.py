import sqlite3

from add_recipe import	add_recipe

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
				break

	except Exception as e:
		print(f"Error: {e}")
		

main()

