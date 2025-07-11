import os

from mylibrary.library import Library


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_menu():
    while True:
        print("\n------ Library Menu ------")

        print("1. Add a book")
        print("2. Search for book")
        print("3. Remove book")
        print("4. Show books")
        print("5. Exit")

        choice = int(input("\nPlease enter your choose : "))

        if choice == 1:
            clear_terminal()
            t = input("Here we go, Enter your book title : ")
            a = input(f"'{t}' written by : ")
            library.add_book(t, a)
            print(f"\nThe '{t}' book writen by '{a}' successfully added\n")

        elif choice == 2:
            clear_terminal()

        elif choice == 3:
            clear_terminal()
            t = input("Enter book title : ")
            library.remove_book(t)

        elif choice == 4:
            library.show_book()

        elif choice == 5:
            print("Bye bye5")
            exit()
        else:
            clear_terminal()
            print("\nPlease enter current section\n")
            show_menu()


library = Library()

if __name__ == '__main__':
    show_menu()
