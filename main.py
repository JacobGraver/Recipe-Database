class RecipeDatabase():
    

    def main(self):
        cmd_prompt()

    def cmd_prompt():
        choice = input(print(f'What would you like to do?\n(1) Add a new recipe.\n(2)'))

        if choice == '1':
            # TODO write add_recipe function
            print('Yay 1 works')

        elif choice == '2':
        	# TODO write 

        else:
            print('Please make a valid selection.')
            cmd_prompt()

main()
