def categorize_employee(salary):
    if salary > 50000:
        return "High Income"
    elif 30000 <= salary <= 50000:
        return "Medium Income"
    else:
        return "Low Income"
try:
    salary = float(input("Enter employee's salary: ₹"))
    category = categorize_employee(salary)
    print(f"Employee Category: {category}")
except ValueError:
    print("Please enter a valid numerical salary.")
