import os
def display_menu():
    print("\nNote Taking App:")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Clear all Notes")
    print("4. Exit")
    return input("Choose a choice (1-4): ") 

def note_taking_app():
    filename = "notes.txt"
    
    # CONDITION: while True
    # Keeps the menu running until we explicitly break
    while True:
        choice = display_menu()

        # CONDITION: if
        if choice == '1':
            note = input("Write your note: ")
            # 'a' mode appends to the file instead of overwriting
            with open(filename, "a") as f:
                f.write(note + "\n")
            print("Note saved.")

        elif choice == '2':
            if os.path.exists(filename):
                print("\n--- Reading Notes ---")
                with open(filename, "r") as f:
                    print(f.read())
            else:
                print("No notes found yet.")

        elif choice == '3':
            # 'w' mode opens the file and wipes it clean
            with open(filename, "w") as f:
                f.write("")
            print("All notes deleted.")

        elif choice == '4':
            print("Goodbye!")
            # CONDITION: break
            # This stops the 'while True' loop
            break

        # CONDITION: else
        # Catches anything that isn't 1, 2, 3, or 4
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
Add file saving feature

    note_taking_app()
