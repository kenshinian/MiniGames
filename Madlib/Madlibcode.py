import madlibtate,simplemadlib

user_choice = input("Enter 1 for Madlibtate or 2 for simplemadlib: ")
if user_choice == "1":
        m = madlibtate
        m.madlib()
elif user_choice == "2":
        m =simplemadlib
        m.madlib()
else:
        print("Invalid choice. Please enter 1 or 2.")
        exit()
