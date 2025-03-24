correct_pin = 1234
attempts = 3 

for i in range(attempts):
    pin = int(input("Enter your 4-digit ATM PIN: "))

    if pin == correct_pin:
        print("Access Granted! Welcome to your account.")
        break
    else:
        remaining_attempts = attempts - (i + 1)
        if remaining_attempts > 0:
            print(f"Incorrect PIN! You have {remaining_attempts} attempts left.")
        else:
            print("Incorrect PIN! Your card has been blocked.")