import add_recipe
import view_all
import search
import update


def main():
    cmd_prompt()


def cmd_prompt():
    choice = input(
        print(
            """
What would you like to do?
(1) Add a new recipe?
(2) View all recipes?
(3) Search for a recipe?
(4) Update a recipe?
(5) Delete a recipe?
"""
        )
    )
    if choice == "1":
        add_recipe.add_recipe()

    elif choice == "2":
        view_all.view_all_recipes()

    elif choice == "3":
        # I believe that I fixed this function
        search.search_recipe()

    elif choice == "4":
        update.update_recipe()

    elif choice == "5":
        # TODO write delete_reipe function
        # This one should be super easy and just an os module
        print("Yay 5 works")

    else:
        print("Please make a valid selection")
        cmd_prompt()


main()
