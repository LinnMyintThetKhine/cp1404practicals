total = 0
number_of_items = int(input("Number of item: "))

while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of item: "))

for i in range(number_of_items):
    prices = float(input("price of item: "))
    total += prices

if total >100:
    total *= 0.9

print("Total price for ", number_of_items, "items is ", total)
