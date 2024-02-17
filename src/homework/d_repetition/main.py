
from repetition import get_factorial, sum_odd_numbers

# Function to display the menu and handle user input
def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter a number (1 to 10): "))
            if 1 <= num <= 10:
                print("Factorial of", num, "is", get_factorial(num))
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        elif choice == '2':
            num = int(input("Enter a number (1 to 100): "))
            if 1 <= num <= 100:
                print("Sum of odd numbers up to", num, "is", sum_odd_numbers(num))
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        elif choice == '3':
            option = input("Do you want to exit? (yes/no): ")
            if option.lower() == 'yes':
                print("Exiting...")
                break
            elif option.lower() == 'no':
                display_menu()
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    display_menu()

if __name__ == "__main__":
    main()