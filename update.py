import json


def update_recipe():
    import main

    # Get the name of the recipe to be updated
    name = input(
        print("What is the name of the recipe that you would like to update? ")
    )

    directory = "Recipe-Database/Recipes"
    file_name = name + ".json"

    if file_name in directory:
        with open(file_name, "r") as f:
            loaded_dict = json.load(f)

        print(loaded_dict[name])

        # choosing which part of the recipe to update
        part = input(
            print("What part of the recipe would you like to update? "))

        # getting the change
        change = input(print("Please type the changed verion now"))

        # Making the change
        loaded_dict[part] = change

    with open(file_name, "r") as f:
        loaded_dict = json.load(f)

    to_change = input(
        print("What part of the recipe would you like to change?"))

    change = input(print("Please type the changed verion now"))

    loaded_dict[to_change] = change

    # load the json string into a file
    with open(file_name, "w") as f:
        loaded_dict = json.load(f)

    main.cmd_prompt()
