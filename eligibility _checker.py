age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible.")
elif age >= 13:
    consent = input("Do you have parental consent? (yes/no): ")
    if consent.lower() == "yes":
        print("You are eligible with consent.")
    else:
        print("You are not eligible.")
else:
    print("You are not eligible.")
