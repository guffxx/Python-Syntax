coins = 100
bills = 150


def calculate_total(coins, bills):
    total = coins + bills
    return total


myTotal = calculate_total(coins, bills)

if myTotal >= 200:
    print(f"Total is over 200: {myTotal}")
else:
    print(f"Total is under 200: {myTotal}")
