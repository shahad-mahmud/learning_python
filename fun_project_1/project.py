def register(file_name:str):
    user_name = input("Enter your user name: ")
    
    user_details_file = open(file_name, "r+")
    names = user_details_file.readlines()
    
    # Check if user name is already registered
    for name in names:
        if user_name == name.strip():
            print("User name already exists. Try again with another user name.")
            return
        
    # User name is not registered. Add in the file
    user_details_file.write(user_name + "\n")
    print('You are successfully registered')
    user_details_file.close()

if __name__ == '__main__':
    option_prompt = "Choose an option from the list:\n\
    \t1. Register\n\
    \nEnter an option: "

    option = int(input(option_prompt))
    user_details_file_name = 'user_details.txt'

    if option not in [1]:
        print("Invalid option. Please try again")
        
    if option == 1:
        register(user_details_file_name)
