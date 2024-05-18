import json


def search_recipe():
    import main

    name = input(
        print("What is the name of the recipe that you are looking for? "))
    directory = "Recipe-Database/Recipes"

    file_name = name + ".json"

    if file_name in directory:
        with open(file_name, "r") as f:
            loaded_dict = json.load(f)

        print(loaded_dict[name])

    main.cmd_prompt()


# First I am going to have to search for the file
# then I will pull it into a dictionary
# then format the dict so that it prints right
# print it and call back to the cmd_line
