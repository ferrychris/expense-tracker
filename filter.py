# • Categorize transactions such as food, transport, and bills
from addtran import expenselist, incomeamount
from addtran import expenseamountlist
from addtran import incomeamount

import json

FoodMatter = []
TransportMatter = []
EntertainmentMatter = []
BillsMatter = []


jsonconv = {
    "food": FoodMatter,
    "transport": TransportMatter,
    "entertainment": EntertainmentMatter,
    "bills": BillsMatter
}
for item in expenselist :
    if item == "FOOD":
        FoodMatter.append(item)
        print("Food expense: ", item)
        print("Food matter: ", FoodMatter)
    elif item == "TRANSPORT":
        TransportMatter.append(item)
        print("Transport expense: ", item)
        print("Transport matter: ", TransportMatter)
    elif item == "ENTERTAINMENT":
        EntertainmentMatter.append(item)
        print("Entertainment expense: ", item)
    elif item == "BILLS":
        BillsMatter.append(item)
        print("Bills expense: ", item)
    else:
        print("Unknown expense: ", item)
        
with open("bills.json", "w") as file:
    json.dump(jsonconv, file, indent=4)

print (f"Your Total income is: ${incomeamount} and your  total expenses are: ${sum(expenseamountlist)}")
if incomeamount > sum(expenseamountlist):
    print("U legit... you actually saved some money")
else:
    print("You spent more than you earned; hope no be woman cause this thing.")
