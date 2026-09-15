pin = input("Enter PIN: ")
balance = 5000
if pin == "1234":
    amount = int(input("Amount: "))
    if amount <= balance:
        print(f"New balance: {balance - amount}")
    else:
        print("Insufficient funds")
else:
    print("Incorrect PIN")
