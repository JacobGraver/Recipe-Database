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
	try:
		choice = input(f"What would you like to do?\n1. Select a recipe\n2. Add a recipe\n3. Change a recipe\n4. Delete a recipe\n5. Exit\n")

		# TODO add the if statements for selections after the functions are made
		if (choice == '1'):
			# TODO make the select recipe function
			print("thank for choose 1")
		elif(choice == '2'):
			print("thank for choose 2")
		elif(choice == '3'):
			print("thank for choose 3")
		elif(choice == '4'):
			print("thank for choose 4")
		elif(choice == '5'):
			print("thank for choose 5")
		else:
			print("Please enter a valid selection.")

		
		
	except Exception as e:
		print(f"Error: {e}")
		

def add_recipe():
	recipe_name = input(f"What is the name of the recipe?\n")
	
main()
