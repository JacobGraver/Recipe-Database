import sqlite_utils

# Create a new database file
db = sqlite_utils.Database("recipes.db")

# Define table schema
recipes_schema = {
    "RecipeID": int,
    "RecipeName": str,
    "PrepTime": int,
    "CookTime": int,
    "Instructions": str,
}

ingredients_schema = {
    "IngredientID": int,
    "IngredientName": str,
}

recipe_ingredients_schema = {
    "RecipeID": int,
    "IngredientID": int,
    "Quantity": str,
}

# Create tables
db["Recipes"].create_table(recipes_schema)
db["Ingredients"].create_table(ingredients_schema)
db["RecipeIngredients"].create_table(recipe_ingredients_schema)
