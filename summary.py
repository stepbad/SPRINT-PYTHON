# Description: Corporate Summary for Revenues and Expenses of HAB Taxi Services
# Author: Braeden Mercer
# Dates(s): August 7th 2024


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants
CUR_DATE = datetime.datetime.now()
HST_RATE = .15
OTHER_EXP = ["Internet and Phone", "Marketing", "Utilities", "Office Supplies"]


# Main report processing starts here

# Generate Report Headings 
print()
print("HAB Taxi Services Corporation")
print(f"Corporate Summary for Revenues and Expenses as of {FV.FDateM(CUR_DATE):<9s}")
print()

# Initialize Revenue Counters and Accumulators

mthFeeCtr = 0
mthFeeAcc = 0
fareCtr = 0
fareAcc = 0
shuttleCtr = 0
shuttleAcc = 0

# Initialize Expenses Counters and Accumulators

fuelCtr = 0
fuelAcc = 0
maintenanceCtr = 0
maintenanceAcc = 0
insuranceCtr = 0
insuranceAcc = 0
otherExpCtr = 0
otherExpAcc = 0


# Open the data files

f = open("Revenues.dat", "r")
g = open("Expenses.dat", "r")

    # Process each line (record) in the file in a loop
for revRecord in f:
    
    revLst = revRecord.split(",")
    revType = revLst[2].strip()
    revAmount = float(revLst[4].strip())


    # Update Counters and Accumulators

    if revType == "Monthly Stand Fees":
        mthFeeCtr += 1
        mthFeeAcc += revAmount

    if revType == "Taxi Fare":
        fareCtr += 1
        fareAcc += revAmount


    if revType == "Airport Shuttle":
        shuttleCtr += 1
        shuttleAcc += revAmount

for expRecord in g:

    expLst = expRecord.split(",")
    expType = expLst[4].strip()
    expAmount = float(expLst[5].strip())

    # Update Counters and Accumulators
    if expType == "Fuel":
        fuelCtr += 1
        fuelAcc += expAmount

    if expType == "Vehicle Maintenance":
        maintenanceCtr += 1
        maintenanceAcc += expAmount

    if expType == "Insurance Premium":
        insuranceCtr += 1
        insuranceAcc += expAmount

    if expType in OTHER_EXP:
        otherExpCtr += 1
        otherExpAcc += expAmount

    # Close the data files

f.close()
g.close()

    # Perform Required Calculations

revSubTot = mthFeeAcc + fareAcc + shuttleAcc
expSubTot = fuelAcc + maintenanceAcc + otherExpAcc
netIncome = revSubTot - expSubTot

revHst = revSubTot * HST_RATE
expHst = expSubTot * HST_RATE
netIncomeHst = netIncome * HST_RATE

revTot = revSubTot + revHst
expTot = expSubTot + expHst
netIncomeTot = netIncome + netIncomeHst


    # Display results

print()
print(f"   Revenue Type          Number of Transactions            Amount")
print()
print(f"---------------------------------------------------------------------")
print(f"Monthly Stand Fee Revenue:        {mthFeeCtr}                           {FV.FDollar2(mthFeeAcc)}")
print(f"Taxi Fare Revenue:               {fareCtr}                           {FV.FDollar2(fareAcc)}")
print(f"Airport Shuttle Revenue:          {shuttleCtr}                           {FV.FDollar2(shuttleAcc)}")
print(f"=====================================================================")
print(f"Subtotal:                                                   {FV.FDollar2(revSubTot)}")
print(f"HST:                                                          {FV.FDollar2(revHst)}")
print(f"Total Revenue:                                              {FV.FDollar2(revTot)}")
print()
print()
print(f"   Expense Type          Number of Transactions            Amount")
print()
print(f"---------------------------------------------------------------------")
print(f"Fuel Costs:                       {fuelCtr}                         {FV.FDollar2(fuelAcc)}")
print(f"Vehicle Maintenance Costs:        {maintenanceCtr}                           {FV.FDollar2(maintenanceAcc)}")
print(f"Insurance Premiums:               {insuranceCtr}                         {FV.FDollar2(insuranceAcc)}")
print(f"Other Expenses:                   {otherExpCtr}                         {FV.FDollar2(otherExpAcc)}")
print(f"=====================================================================")
print(f"Subtotal:                                                   {FV.FDollar2(expSubTot)}")
print(f"HST:                                                          {FV.FDollar2(expHst)}")
print(f"Total Expenses:                                             {FV.FDollar2(expTot)}")
print()
print()
print(f"---------------------------------------------------------------------")
print(f"Net Income:                                                {FV.FDollar2(netIncome)}")
print()
print()

# Any housekeeping duties at the end of the program