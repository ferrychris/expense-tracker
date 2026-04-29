income = []
expenseamountlist = []
expenselist = []
incomeamount = 0

spender = str(input("what did you spend on(Food, Transport, Entertainment, bills only.): ").upper())
if spender != "FOOD" and spender != "TRANSPORT" and spender != "ENTERTAINMENT" and spender != "BILLS":
    print("Invalid input")
    spender = str(input("what did you spend on(Food, Transport, Entertainment, bills only.): ").upper())
    expenseoutput = expenselist.append(spender)
else: 
    expenselist.append(spender)
    spendamount = int(input("how much did you spend: "))
    expenseamountoutput= expenseamountlist.append(spendamount)

# loopcheckspend = bool(input("Do you want to add another expense? (y/n): "))
# loopcheckspendamount = bool(input("add amount for the expense: "))
for i in range(10):
    pass
loopcheckspend =(input("Do you want to add another expense? (y/n): "))

if loopcheckspend == "y":
    spender = str(input("what did you spend on(Food, Transport, Entertainment, bills only.): ").upper())
    expenseoutput= expenselist.append(spender)
    spendamount = int(input("how much did you spend: "))
    expenseamountoutput= expenseamountlist.append(spendamount)
elif loopcheckspend == "n":
    print("No more expenses added.")
else:
    exit()


incomeamountinput = int(input("how much is your income: "))
incomeamount = incomeamountinput


# Calculation time

# expenseoutput= expenselist.append(spender)
# expenseamountoutput= expenseamountlist.append(spendamount)



# print(expenseoutput)
# print(expenseamountoutput)
