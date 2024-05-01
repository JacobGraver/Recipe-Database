import json


def update_recipe():
    import main

    # Get the name of the recipe to be updated
    name = input(
        print("What is the name of the recipe that you would like to update? ")
    )

    # File details
    directory = "Recipe-Database/Recipes"
    file_name = name + ".json"

    # If the file is in the folder then read it into a dictionary
    if file_name in directory:
        with open(file_name, "r") as f:
            loaded_dict = json.load(f)

        print(loaded_dict[name])

        # choosing which part of the recipe to update
        # Formatting is odd because the line is too long otherwise
        part = input(
            print("""
        What part of the recipe would you like to update?
        """)
        )

        # getting the change
        change = input(print("Please type the changed verion now: "))

        # Making the change
        loaded_dict[part] = change

    # load the json string into a file
    with open(file_name, "w") as f:
        loaded_dict = json.load(f)

    main.cmd_prompt()
