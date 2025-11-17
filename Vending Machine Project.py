beverageList = ["Cola", "Lemon-Lime", "Orange", "Cherry", "Grape", "Sparkling Water"]
beveragePrice = float(2.99)
beverage = 0
print("The following beverages are available: 1. Cola, 2. Lemon-Lime, 3. Orange, 4. Cherry, 5. Grape, 6. Pepper Soda")
while beverage !=7:
    beverage = int(input("Please choose a beverage:\n"))
    if beverage == 1:
        print("You have picked:", beverageList[0])
    elif beverage == 2:
        print("You have picked:", beverageList[1])
    elif beverage == 3:
        print("You have picked:", beverageList[2])
    elif beverage == 4:
        print("You have picked:", beverageList[3])
    elif beverage == 5:
        print("You have picked:", beverageList[4])
    elif beverage == 6:
        print("You have picked:", beverageList[5])
    print("The total amount due is", beveragePrice)

    amountCollected = float(input("Please enter an amount: "))
    while amountCollected < 2.99:
        amountDue = beveragePrice - amountCollected
        print("The amount due is now", round(amountDue,2))
        amountCollected += float(input("Please enter an amount:\n"))
    if amountCollected == 2.99:
        print("Your drink has been dispensed. Enjoy!")
    if amountCollected > 2.99:
        change = amountCollected - beveragePrice
        print("Your drink has been dispensed. Your total change is", round(change,2), "Enjoy!")