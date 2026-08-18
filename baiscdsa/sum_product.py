listItems = [1, 2, 3, 4, 5]

sum = 0
product = 1
for item in listItems:
    sum += item

for item in listItems:
    product *= item

print(f"Sum of all items: {sum}")
print(f"Product of all items: {product}")
