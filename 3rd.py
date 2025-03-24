
balance = 10000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print(f"Your current balance is ₹{balance}")

    elif choice == 2:
        deposit = float(input("Enter the amount to deposit: ₹"))
        if deposit > 0:
            balance += deposit
            print(f"₹{deposit} deposited successfully. New balance: ₹{balance}")
        else:
            print("Invalid deposit amount!")

    elif choice == 3:
        withdraw = float(input("Enter the amount to withdraw: ₹"))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f"₹{withdraw} withdrawn successfully. Remaining balance: ₹{balance}")
        elif withdraw > balance:
            print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount!")

    elif choice == 4:
        print("Exiting the ATM system. Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")