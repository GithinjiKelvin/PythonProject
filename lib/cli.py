from helpers import(
    exit_program,
    list_apartments,
    find_apartment_by_name,
    find_apartment_by_id,
    add_apartment,
    update_apartment,
    delete_apartment
)

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_apartments()
        elif choice == "2":
            find_apartment_by_name()
        elif choice == "3":
            find_apartment_by_id()
        elif choice == "4":
            add_apartment()
        elif choice == "5":
            update_apartment()
        elif choice == "6":
            delete_apartment()


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all the apartments")
    print("2. Find apartment by name")
    print("3. Find apartment by id")
    print("4. Add new apartment")
    print("5. Update an existing apartment")
    print("6. Delete an existing apartment")




if __name__ == "__main__":
    main()