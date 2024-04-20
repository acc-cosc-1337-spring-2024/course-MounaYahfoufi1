#
import sys
from class_a import Die 

def main():
    die = Die()
    while True:
        die.roll()  # Roll the die
        print(f"The rolled value is: {die.get_rolled_value()}")  # Display the roll result

        # Prompt the user if they want to continue
        continue_choice = input("Roll again? Enter 'yes' to continue or any other key to exit: ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program. Thank you for playing!")
            break

if __name__ == "__main__":
    main()
