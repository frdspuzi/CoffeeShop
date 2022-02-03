from menu import MENU
from menu import resources
from art import logo
import time

order = ""
mode = "ON"
status = False
total = 0
userCoins = 0
sufficient = False
userInput= ""

def clc():
    print("\033c")

#check if integer
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break

#print report
def printReport():
    print(f'''Resources left:
    Water: {resources['water']} ml
    Milk: {resources['milk']} ml
    Coffee: {resources['coffee']} g
    Money: ${total}
    ''')

#check resources sufficient
def checkResources(order):

    if order != 'espresso':

        if (int(MENU[order]['ingredients']['milk']) > int(resources['milk'])): 
            print(f"UNSUCCESSFUL. Sorry, there is not enough milk.")
            return False

        if (int(MENU[order]['ingredients']['water']) <= int(resources['water'])) and (int(MENU[order]['ingredients']['milk']) <= int(resources['milk'])) and (int(MENU[order]['ingredients']['coffee']) <= int(resources['coffee'])):
            print(f"SUCCESSFUL. Payment for {order} is pending.")
            return True

    if (int(MENU[order]['ingredients']['water']) > int(resources['water'])): 
        print(f"UNSUCCESSFUL. Sorry, there is not enough water.")
        return False

    if (int(MENU[order]['ingredients']['coffee']) > int(resources['coffee'])):
        print(f"UNSUCCESSFUL. Sorry, there is not enough coffee.")
        return False

    else:
        if (int(MENU[order]['ingredients']['water']) <= int(resources['water'])) and (int(MENU[order]['ingredients']['coffee']) <= int(resources['coffee'])):
            print(f"SUCCESSFUL. Payment for {order} is pending.")
            return True

        # if (int(MENU[order]['ingredients']['water']) > int(resources['water'])): 
        #     print(f"UNSUCCESSFUL. Sorry, there is not enough water.")
        #     return False

        

        # if (int(MENU[order]['ingredients']['coffee']) > int(resources['coffee'])):
        #     print(f"UNSUCCESSFUL. Sorry, there is not enough coffee.")
        #     return False

        
#process coins
def processCoins():

    quarters= int(inputNumber("Quarters ($0.25): "))
    dimes= int(inputNumber("Dimes ($0.10): "))
    nickles= int(inputNumber("Nickles ($0.05): "))
    pennies= int(inputNumber("Pennies ($0.01): "))

    userCoins= quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    
    return userCoins

#check transaction successful
def checkTransaction(userCoins,order):

    if userCoins < float(MENU[order]['cost']):
        print("You don't have enough coins.")
        return False,

    elif userCoins > float(MENU[order]['cost']):
        balance = userCoins - float(MENU[order]['cost'])
        print(f"balance= {userCoins} - {MENU[order]['cost']}")
        print("Transaction Successful. Your balance is: $",balance)
        return True

    else:
        print("Transaction Successful.")
        return True

#make coffee
def makeCoffee(order):
    resources['water'] = resources['water'] - int(MENU[order]['ingredients']['water'])
    
    if order != 'espresso':
        resources['milk'] = resources['milk'] - int(MENU[order]['ingredients']['milk'])
    
    resources['coffee'] = resources['coffee'] - int(MENU[order]['ingredients']['coffee'])
    total =+ float(MENU[order]['cost'])

    print(f"\nHere is your {order}. Enjoy!")

    time.sleep(3)
    clc()
    print(logo)

    return total

clc()
print(logo)

while (userInput != "espresso") or (userInput != "latte") or (userInput != "cappuccino") or (userInput != "report"): 
    
    userInput= input(f'''MENU: 

    - Espresso (${MENU['espresso']['cost']})  
    - Latte (${MENU['latte']['cost']})
    - Cappuccino (${MENU['cappuccino']['cost']})

    What would you like?
    ''')

    userInput= userInput.lower()

    if (userInput == "espresso") or (userInput == "latte") or (userInput == "cappuccino"):
        order= userInput
    
        sufficient= checkResources(order)

        if sufficient == True:
            userCoins = processCoins()
            status = checkTransaction(userCoins,order)
            if status == True:
                total= makeCoffee(order)
        #   else:
        #         break
        # else:
        #     break

    elif (userInput == "report"):
        printReport()

