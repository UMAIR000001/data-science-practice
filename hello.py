user = input("Did you forget the Python basic concept [Yes/No]: ")
user = user.strip().lower()  

if user in ["yes", "y"]:
    print("Mashallah Umair")
elif user in ["no", "n"]:
    print("Not Good Umair!")
else:
    print("Invalid input! Please enter Yes or No.")
