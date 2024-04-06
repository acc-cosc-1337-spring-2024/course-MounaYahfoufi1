#
from sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog2,get_students_who_took_prog2_not_prog1

def main_menu():
    while True:
        print("\nInventory Menu\n")
        print("1-Students who took prog1 and prog2")
        print("2-Students who took prog2 only")
        print("3-Students who took prog1 not prog2")
        print("4-Students who took prog2 not prog1")
        print("5-Exit\n")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == "1":
            print(f"Students who took both prog1 and prog2: {get_students_who_took_prog1_and_prog2(prog1, prog2)}")
        elif choice == "2":
            print(f"Students who took prog2 only (not prog1): {get_students_who_took_prog2_not_prog1(prog1, prog2)}")
        elif choice == "3":
            print(f"Students who took prog1 and not prog2: {get_students_who_took_prog1_not_prog2(prog1, prog2)}")
        elif choice == "4":
            print(f"Students who took prog2 and not prog1: {get_students_who_took_prog2_not_prog1(prog1, prog2)}")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    # Define the program sets
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}
    
    # Run the main menu
    main_menu()
