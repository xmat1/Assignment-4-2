# Get user input
employeeName = input("Enter Employee Name: ")
numShifts = int(input("Enter Number of Shifts: "))
numTransactions = int(input("Enter Number of Transactions: "))
transactionValue = float(input("Enter Transaction Dollar Value: "))

# Calculate productivity score
productivityScore = (transactionValue / numTransactions) / numShifts

# Determine bonus
if productivityScore <= 30:
    bonus = 50.00
else:
    if productivityScore <= 69:
        bonus = 75.00
    else:
        if productivityScore <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

# Output
print("\nEmployee Name:", employeeName)
print("Employee Bonus: $" + str(bonus))