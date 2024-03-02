#
from strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("\nMenu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            try:
                distance = get_hamming_distance(dna1, dna2)
                print("The Hamming Distance is:", distance)
            except ValueError as e:
                print(e)

        elif choice == '2':
            dna = input("Enter a DNA string: ")
            complement = get_dna_complement(dna)
            print("The DNA Complement is:", complement)

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
