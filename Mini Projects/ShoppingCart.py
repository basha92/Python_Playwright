#using while loop and lists

#res = "\n".join("{} {}".format(x, y) for x, y in zip(a, b)) - joining 2 lists

foods=[]
prices=[]
total=0

while True:
    food = input("Enter the food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
        result = "\n".join("{}: $ {}".format(x, y) for x, y in zip(foods, prices))
        total = total+price

print("------YOUR CART-----")
print(result)
print("Total: ", total)