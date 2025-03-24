amount = int(input("Enter the amount to withdraw (multiple of 500): "))

if amount % 500 != 0:
    print("Invalid amount! Please enter a multiple of 500.")
else:
    notes_2000 = amount // 2000
    remaining = amount % 2000 
    notes_500 = remaining // 500

    print(f"₹2000 notes: {notes_2000}")
    print(f"₹500 notes: {notes_500}")
