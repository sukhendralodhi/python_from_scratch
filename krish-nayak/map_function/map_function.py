# map(): The map() function in Python is used to apply a given function to each item of an iterable (like a list or tuple) and return a map object (which is an iterator) containing the results.

# Example:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# iterate over tuple
numbers_tuple = (1, 2, 3, 4, 5)
squared_numbers_tuple = tuple(map(lambda x: x**2, numbers_tuple))
# print(squared_numbers_tuple)  # Output: (1, 4, 9, 16, 25)

prices = [50, 120, 80, 200, 30, 150]

def check(price):
        # print(price)
    if price > 100:
        return price


# print(high_price)

highPrices = list(filter(check, prices))
print(highPrices)
