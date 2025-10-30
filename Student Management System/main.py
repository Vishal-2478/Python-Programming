import utils

def main():
    while(1):
        utils.show_menu()
        choice = input("Enter your choice: ")
        utils.perform_operation(choice)
        if choice == '5':
            break

if __name__ == "__main__":
    main()