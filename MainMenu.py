# Description: Create a code for a menu-based system to run the different programs, Employee, Revenues, Expenses, Cars, Payments, Profits, Financials, and Summary Report.  Q2 Final Sprint. 

# Author: Stephen Badcock, SD-12: Robot Group-7.

# Date(s): July 31, 2024 - August 12, 2024


# Define required libraries.
import datetime
import os

# Constants for file names
EMPLOYEES_FILE = "Employees.dat"
REVENUES_FILE = "Revenues.dat"
EXPENSES_FILE = "Expenses.dat"

# Function to read employees from file
def read_employees():
    employees = []
    if os.path.exists(EMPLOYEES_FILE): #TabNine suggested this part
        with open(EMPLOYEES_FILE, "r") as file:
            for line in file:
                data = line.strip().split(",")
                employee = {
                    "driver_number": data[0],
                    "name": f"{data[1]} {data[2]}"
                    "own_car": data[9] == "Y",
                    "balance_due": float(data[10])
                }
                employees.append(employee)
    return employees

# Function to write employees to file
def write_employees(employees):
    print("I will come back to this part after finishing any other work.")

# Function to read revenues from file
def read_revenues():
    revenues = []
    if os.path.exists(REVENUES_FILE): #TabNine suggested this
        with open(REVENUES_FILE, "r") as file:
            for line in file:
                # Assuming each line is a comma-separated record
                data = line.strip().split(",")
                revenue = {
                    "transaction_id": data[0],
                    "date": data[1],
                    "description": data[2],
                    "driver_number": data[3],
                    "amount": float(data[4]),
                    "hst": float(data[5]),
                    "total": float(data[6])
                }
                revenues.append(revenue)
    return revenues

# Function to write revenues to file
def write_revenues(revenues):
    print("If I have time after everything else.")

# Function to apply stand fees on the first of each month
def apply_stand_fees():
    today = datetime.date.today()
    # Check if today is the first of the month
    if today.day == 1:
        employees = read_employees()
        revenues = read_revenues()
        # Apply stand fees for each employee with their own car
        for employee in employees:
            if employee["own_car"]:
                stand_fee = 175.00
                hst = stand_fee * 0.15  # Assuming 15% HST
                total = stand_fee + hst
                employee["balance_due"] += total

                # Create a revenue entry
                revenue = {
                    "transaction_id": str(len(revenues) + 1),
                    "date": str(today),
                    "description": "Monthly Stand Fees",
                    "driver_number": employee["driver_number"],
                    "amount": stand_fee,
                    "hst": hst,
                    "total": total
                }
                revenues.append(revenue)
        
        # Update files with new balances and revenue records
        write_employees(employees)
        write_revenues(revenues)
        print("Stand fees applied and records updated.")
    else:
        print("Today is not the first of the month. No stand fees applied.")

while True:
    print("\nHAB Taxi Services - Company Services System")
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Corporate Summary Report.")
    print("9. Quit Program.")
    
    choice = input("Enter choice (1-9): ")
    
    if choice == "1":
        import menuitem1FinalSprint          
        print("Enter a New Employee functionality.")
    elif choice == "2":
        # Placeholder for Enter Company Revenues functionality
        print("Enter Company Revenues functionality.")
    elif choice == "3":
        # Placeholder for Enter Company Expenses functionality
        print("Enter Company Expenses functionality.")
    elif choice == "4":
        # Placeholder for Track Car Rentals functionality
        print("Track Car Rentals functionality.")
    elif choice == "5":
        # Placeholder for Record Employee Payment functionality
        print("Record Employee Payment functionality.")
    elif choice == "6":
        # Placeholder for Print Company Profit Listing functionality
        print("Print Company Profit Listing functionality.")
    elif choice == "7":
        import DrivFinList
        print("Print Driver Financial Listing functionality.")
    elif choice == "8":
        # Placeholder for Corporate Summary Report functionality
        print("Corporate Summary Report functionality.")
    elif choice == "9":
        # Quit the program
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")



# Any housekeeping duties at the end of the program.

print("Goodbye!")
