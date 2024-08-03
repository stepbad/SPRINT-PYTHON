# Description: Create a code for a menu-based system to run the different programs, Employee, Revenues, Expenses, Cars, Payments, Profits, Financials, and Summary Report.  Q2 Final Sprint. 

# Author: Stephen Badcock, SD-12: Robot Group-7.

# Date(s): July 31, 2024 - August 12, 2024


# Define required libraries.


# Define program constants.



# Define program functions.


# Main program starts here.
while True:
    
    print()
    print(f"          Final Sprint - Main Menu")
    print(f"             HAB Taxi Services")
    print(f"          Company Services System")
    print(f"------------------------------------------------")
    print( )
    print(f"     1. Enter a New Employee (driver).")
    print(f"     2. Enter Company Revenues.")
    print(f"     3. Enter Company Expenses.")
    print(f"     4. Track Car Rentals.")
    print(f"     5. Record Employee Payment.")
    print(f"     6. Print Company Profit Listing.")
    print(f"     7. Print Driver Financial Listing.")
    print(f"     8. Corporate Summary Report.")
    print(f"     9. Quit Program.")
    print()
    print(f"------------------------------------------------")
    print()
    Choice = input("Enter choice (1-9):  ")
    Choice = int(Choice)

    print()
    print()


    if Choice == 1:
        import NewEmployee
    
    if Choice == 2:
        import CompanyRevenues

    if Choice == 3:
        import CompanyExpenses

    if Choice == 4:
        import CarRentals

    if Choice == 5:
        import EmployeePayments

    if Choice == 6:
        import ProfitListing

    if Choice == 7:
        import DriverFinancialListing

    if Choice == 8:
        import CorporateSummaryReport

    if Choice == 9:
        print("Thank you for using HAB Taxi Services.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
        print()
        continue
        
    
    

# Any housekeeping duties at the end of the program.

print("Goodbye!")