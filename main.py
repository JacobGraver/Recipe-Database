import add_recipe
import view_all


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
        # TODO write search_recipe function
        print('Yay 3 works')

    elif choice == '4':
        # TODO write update_recipe function
        print('Yay 4 works')
        
    elif choice == '5':
        # TODO write delete_recipe function
        print('Yay 5 works')
        
    else:
        print('Please make a valid selection')
        cmd_prompt()


main()
