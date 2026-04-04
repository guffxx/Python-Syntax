while True:
    coins_input = input("How many coins do you have? ")
    bills_input = input("How many bills do you have? ")
    if coins_input.isdigit() and bills_input.isdigit():
        coins = int(coins_input)
        bills = int(bills_input)
        break
    else:
        print("Invalid input. Please enter a valid number.")
        continue


print(coins)
print(bills)


myTotal = coins + bills

match myTotal:
    case n if n > 100:
        print(f"Total is over 100: {myTotal}")
    case n if n < 100:
        print(f"Total is below 100: {myTotal}")
