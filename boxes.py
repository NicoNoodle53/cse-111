import math

#ask for the items and items per box used
items = int(input("Enter the number of items: "))
items_per = int(input("Enter the number of itmes per box: "))

# calculate how many boxes will be needed
boxes = items/items_per

# print results
print(f"For {items} items, packing {items_per} items in each box, you will need {math.ceil(boxes)} boxes.")