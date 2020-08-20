"""
This program calculates the total price for a number of items
"""
"""Kevin Hinds"""
total_cost = 0

"""Inputs number of items and calculates total cost before and discount"""

number_of_items = int(input("Please enter of items:"))

"""Error checking for inputs less than 0"""
while number_of_items < 0:
    number_of_items = int(input("Invalid number of items! Please enter of items:"))
for i in range(number_of_items):
    cost_of_item = float(input("Please enter cost of item: "))
    total_cost = total_cost + cost_of_item
"""Calculates total price after any discount needs to be applied"""
if total_cost > 100:
    total_cost = total_cost * 0.9
print("Total price for ", number_of_items, "items is {:.2f}".format(total_cost))
