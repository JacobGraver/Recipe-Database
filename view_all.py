import os


def view_all_recipes():
    all = os.listdir("/home/myth/Git/Recipe-Database/Recipes")
    print(all)
