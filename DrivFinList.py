# Code for printing a drivers financial listing
# Author: Christopher King, Stephen Badcock
# August, 07, 2024

import datetime

# Constants for file paths
EMPLOYEE_FILE = 'Employees.dat'  # driver number, name, address, phone number, etc.
REVENUE_FILE = 'Revenues.dat'    # Transaction ID, date, description, driver number, amount, HST, Total
EXPENSES_FILE = 'Expenses.dat'   # Invoice number, date, driver number, item number, description, cost, quantity, total

def parse_date(date_str):
    """Convert a string date to a datetime.date object."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

def load_employees():
    """Load employee data from file."""
    employees = {}
    try:
        with open(EMPLOYEE_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                driver_ident = parts[0]
                name = f"{parts[1]} {parts[2]}"
                employees[driver_ident] = name
    except FileNotFoundError:
        print(f"Error: {EMPLOYEE_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while reading {EMPLOYEE_FILE}: {e}")
    return employees

def calculate_revenue_by_driver(driver_id, start_date, end_date):
    """Calculate total revenue by driver."""
    total_revenue = 0.0
    try:
        with open(REVENUE_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                trans_date = parse_date(parts[1])
                if parts[3] == driver_id and start_date <= trans_date <= end_date:
                    total_revenue += float(parts[4])  # Amount of the transaction
    except FileNotFoundError:
        print(f"Error: {REVENUE_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while reading {REVENUE_FILE}: {e}")
    return total_revenue

def calculate_expenses_by_driver(driver_id, start_date, end_date):
    """Calculate total expenses by driver."""
    total_expenses = 0.0
    try:
        with open(EXPENSES_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                trans_date = parse_date(parts[1])
                if parts[2] == driver_id and start_date <= trans_date <= end_date:
                    total_expenses += float(parts[-1])  # The last part is the total amount including tax
    except FileNotFoundError:
        print(f"Error: {EXPENSES_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while reading {EXPENSES_FILE}: {e}")
    return total_expenses

# Main Program to Generate and print a financial listing report
if __name__ == "__main__":
    employees = load_employees()
    
    while True:
        driver_id = input("Enter the Driver ID or type 'Exit' to end the program: ").strip()
        if driver_id.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if driver_id not in employees:
            print(f"Driver ID {driver_id} not found.")
            continue
        
        start_date_str = input("Enter the start date (YYYY-MM-DD): ").strip()
        end_date_str = input("Enter the end date (YYYY-MM-DD): ").strip()
        
        # Parse dates
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
        
        # Required calculations
        revenue = calculate_revenue_by_driver(driver_id, start_date, end_date)
        expenses = calculate_expenses_by_driver(driver_id, start_date, end_date)
        profit = revenue - expenses
        
        print("\nDriver Financial Listing Report")
        print("=================================================")
        print(f"Driver ID: {driver_id}")
        print(f"Name: {employees[driver_id]}")
        print(f"Total Revenue:  ${revenue:,.2f}")
        print(f"Total Expenses: ${expenses:,.2f}")
        print(f"Net Profit:     ${profit:,.2f}")
        print("-------------------------------------------------")
