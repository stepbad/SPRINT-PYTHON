# Description: Program for taxi stand, The HUB Taxi Services of three brothers to run the business of 
# rental cars and other services.
# Author: Mimya Hafiz
# Date(s): 2024-08-04 to 2024-08-06
 
 
# Define required libraries.
import datetime
import FormatValues as FV
 
import time
import sys

# Define program constants.

#NEXT_TRANS_ID = 143
#NEXT_DRIVER_NUM = 1922
#MONTHLY_STAND_FEE = 175.00
#DAILY_RENTAL_FEE = 60.00
#WEEKLY_RENTAL_FEE = 300.00
#HST_RATE = .15

RentalChoice = ""



# Open the defaults file and read the values into variables
# The file must be created first since it is being read, it must exits. 
def OpenReadDefault(default_file):
    with open(default_file, "r") as file:
        for line in file:
            linelst = line.split(",")
            NEXT_TRANS_ID = int(linelst[0].strip())
            NEXT_DRIVER_NUM = int(linelst[1].strip())
            MONTHLY_STAND_FEE = float(linelst[2].strip())
            DAILY_RENTAL_FEE = float(linelst[3].strip())
            WEEKLY_RENTAL_FEE = float(linelst[4].strip())
            HST_RATE = float(linelst[5].strip())
            return NEXT_TRANS_ID, NEXT_DRIVER_NUM, MONTHLY_STAND_FEE, DAILY_RENTAL_FEE, WEEKLY_RENTAL_FEE, HST_RATE

# Define program functions.

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


 
# Main program starts here.
while True:
   
    # Gather user inputs.
    
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'")     # Employee First Name
    while True:
        EmpFirst = input("Enter the Employee First Name: ").title()
        if EmpFirst == "":
            print("   Data Entry Error - Employee Name cannot be Blank.")
        elif set(EmpFirst).issubset(allowed_char) == False:
            print("   Data Entry Error - Employee Name Contains Invalid Characters.")
        else:
            break 



    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'")       # Employee Last Name
    while True:
        EmpLast = input("Enter the Employee Last Name: ").title()
        if EmpLast == "":
            print("   Data Entry Error - Employee Name cannot be Blank.")
        elif set(EmpLast).issubset(allowed_char) == False:
            print("   Data Entry Error - Employee Name Contains Invalid Characters.")
        else:
            break




    FullName = EmpFirst + " " + EmpLast


    StAdd= input("Enter the Street Address: ").title()
    City = input("Enter the City: ").title()
    

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MN", "SK", "AB", "BC", "YT", "NW", "NT"]
    while True:
        Prov = input("Enter the Province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be Blank - Please Reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 Digit Code - Please Reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a Valid Province - Please Reenter.")
        else:
            break



    Postal = input("Enter the Postal Code (X9X9X9): ").upper()



    allowed_char = set("0123456789")
    while True:
        PhoneNum = input("Enter the Phone Number (9999999999): ")

        if PhoneNum == "":
            print("   Data Entry Error - Phone Number cannot be Blank.")
        elif len(PhoneNum) != 10:
            print("   Data Entry Error - Phone Number must be 10 digits.")
        elif set(PhoneNum).issubset(allowed_char) == False:                                # PhoneNum.isdigit for num, .alpha is for alphabet
            print("   Data Entry Error - Phone Number Contains Invalid Characters.")
        else:
            PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
            break   
         



    LicenseNum = input("Enter the Driver's License Number(#####): ")
    ExpiryDate = input("Enter the Driver's License Expiry Date(YYYY-MM-DD): ")  
   

    InsuranceCompany = input("Enter the Name of Insurance Company: ").title()
    PolicyNum = input("Enter the Insurance Company Policy Number(######): ")
    
    CarStatusLst = ["Y", "N"]
    while True:
        CarStatus = input("Will employee Rent a car? (Y/N): ").upper()

        if CarStatus == "":
            print("   Data Entry Error - Car Status cannot be Blank.")
        elif len(CarStatus) != 1:
            print("   Data Entry Error - Car Status must be 1 Digit Code.")
        elif CarStatus not in CarStatusLst:
            print("Error - Not a Valid Status - Please Reenter.")
        else:
            break
    

    if CarStatus == "Y":
        RentalChoiceLst = ["D", "W"]
        while True:
            RentalChoice = input("Enter the Car's Rental Choice(D/W): ").upper()

            if RentalChoice == "":
                print("   Data Entry Error - Car Rental Choice cannot be Blank.")
            elif len(RentalChoice) != 1:
                print("   Data Entry Error - Car Rental Choice must be 1 Digit Code.")
            elif RentalChoice not in RentalChoiceLst:
                print("Error - Not a Valid Rental Choice - Please Reenter.")
            else:
                break


    # Current Date
    CurDate = datetime.datetime.now()
    InvoiceDate= CurDate.strftime("%Y-%m-%d")

    # Read values from the defaults file.
    NEXT_TRANS_ID, NEXT_DRIVER_NUM, MONTHLY_STAND_FEE, DAILY_RENTAL_FEE, WEEKLY_RENTAL_FEE, HST_RATE = OpenReadDefault("Defaults.dat")


    # Perform required calculations.
    if CarStatus == "N": 
        StandFeeDue = MONTHLY_STAND_FEE
        RentalDue = 0
        
    else:
        StandFeeDue = 0
        if RentalChoice == "D": 
            RentalDue = DAILY_RENTAL_FEE
        
        else:
            RentalDue = WEEKLY_RENTAL_FEE


        

    SubTotal = StandFeeDue + RentalDue
    HST = SubTotal * HST_RATE
    TotMonCharge =  SubTotal + HST

    
    # Display results
    
    # For the Insurance Details Data
    f = open("Employee.dat", "a") #Mode can be 'a' for append, 'w' for overwrite, 'r' to read.
 
    # Any value written to a file must be recognized as a string.
    f.write(f"{str(NEXT_DRIVER_NUM)}, ")
    f.write(f"{InvoiceDate}, ") # This is the current system date

    f.write(f"{FullName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{Postal}, ")
    f.write(f"{PhoneNum}, ")

    f.write(f"{LicenseNum}, ")
    f.write(f"{ExpiryDate}, ")
    f.write(f"{InsuranceCompany}, ")
    f.write(f"{PolicyNum}, ")
    f.write(f"{CarStatus}, ")
    f.write(f"{RentalChoice}, ")

    f.write(f"{SubTotal}, ")
    f.write(f"{HST}, ")
    f.write(f"{TotMonCharge},\n ")
    f.close()


    print()
    print()
    print(f"       --------------------------------------------------------------------------------------------------")
    print(f"                                                 HAB Taxi Services                       ")
    print(f"                                                  Employee Record                         ")
    print(f"       --------------------------------------------------------------------------------------------------")
    print()
    print(f"       Insurance Company: {InsuranceCompany:<10s}                       ")
    print(f"       Insurance Policy No: {PolicyNum:<10s}                         ")
    print(f"       --------------------------------------------------------------------------------------------------")
    print()



    print(f"       {FullName:<20s}                                                     Driving License No: {LicenseNum:<10s}                   ")
    print(f"       {StAdd:<20s}                                                     Expiry Date:   {ExpiryDate:>10s}                           ")  
    print(f"       {City:<20s}, {Prov:<2s}                                                           ")
    print(f"       {Postal:<6s}                                                                                            ")
    print(f"       Phone Number: {PhoneNum:>13s}                                                  ")                                                 
    print(f"       Cell Number:  {CellNum:>13s}                                            Invoice Date:   {InvoiceDate:>10s}")
    print()
    print(f"       ==================================================================================================")


    print()
    
    print(f"       Employee    Car          Stand           Rental          Sub           HST           Total ")
    print(f"       ID          Status       Fee             Fee             Total                       Due")
    print(f"       ==================================================================================================")
    print(f"       {NEXT_DRIVER_NUM:<4d}        {CarStatus:<s}            {FV.FDollar2(StandFeeDue):<10s}      {FV.FDollar2(RentalDue):<10s}      {FV.FDollar2(SubTotal):<10s}    {FV.FDollar2(HST):<10s}    {FV.FDollar2(TotMonCharge):<10s}")
    print()
    
    
    print()
    print()

    print(f"       ------------------------------------------- Thank  You -------------------------------------------")

    print()
    print()


    # Update any values for the next claim.
    # Can place the inside to loop to update each time, or in the housekeeping
    # section below to update when the user exists in the program
    NEXT_DRIVER_NUM += 1
    NEXT_TRANS_ID += 1


    # Write the current values back t the default file. Note the use of “w” to overwrite 
    f = open('Defaults.dat', 'w')
    # Values are stored as strings, covert according
    f.write(f"{NEXT_TRANS_ID}")
    f.write(f"{NEXT_DRIVER_NUM}")

    f.write(f"{MONTHLY_STAND_FEE}")
    f.write(f"{DAILY_RENTAL_FEE}")

    f.write(f"{WEEKLY_RENTAL_FEE}")
    f.write(f"{HST_RATE}\n")
    f.close()

     


    TotalIterations = 30 # The more iterations, the more time is takes.
    Message = "Saving Employee Policy Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()

    
    print()
    print("Employee Policy data has been sucessfully saved.")
    print()
    
    Continue = input("Do you want to process another Employee Record (Y / N): ").upper()
    if Continue == "N":
        break



 
# Any housekeeping duties at the end of the program.
