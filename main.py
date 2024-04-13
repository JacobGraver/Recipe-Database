import add_recipe
import view_all
import search


def main():
    cmd_prompt()
    

def cmd_prompt():
    choice = input(print(f"What would you like to do?\n(1) Add a new recipe\n(2) View all recipes\n(3) Search for a recipe\n(4) Update a recipe\n(5) Delete a recipe"))

    if choice == '1':
        # Calls the add recipe module
        add_recipe.add_recipe()

    elif choice == '2':
        view_all.view_all_recipes()
        
    elif choice == '3':
        search.search_recipe()

    elif choice == '4':
        # TODO write update_recipe function
        # This one could get annoying with figuring out how to let them actively edit (document style) so you dont have to re-type the entire steps
        print('Yay 4 works')
        
    elif choice == '5':
        # TODO write delete_recipe function
        # This one should be super easy and just an os module
        print('Yay 5 works')
        
    else:
        print('Please make a valid selection')
        cmd_prompt()


main()
