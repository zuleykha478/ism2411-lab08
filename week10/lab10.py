# ==========================================
# Module 10 Lab: Inventory List Manager
# Name: Zuleykha Jafarzade
# Reflection Questions:
# 1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
#    Lists can hold mixed data types and are mutable, meaning they change in place without needing a new variable assignment.
# 2. Describe one real business situation where a Python list would have saved time compared to Excel.
#    Processing thousands of retail SKUs and daily sales figures from an ERP download automatically takes seconds, 
#    whereas manual filtering and sorting in Excel can be error-prone and tedious.
# ==========================================

# EXERCISE 1 · Beginner: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print("EXERCISE 1:")
print(inventory)
print(len(inventory))
print("-" * 30)

# EXERCISE 2 · Beginner: Index practice
middle_index = len(inventory) // 2
print("EXERCISE 2:")
print(inventory[0])                  # First
print(inventory[-1])                 # Last
print(inventory[middle_index])       # Middle
print("-" * 30)

# EXERCISE 3 · Beginner: Slicing
print("EXERCISE 3:")
print(inventory[:3])        # First three items
print(inventory[-2:])       # Last two items
print(inventory[::2])       # Every other item (step slice)
print("-" * 30)

# EXERCISE 4 · Intermediate: Modify
print("EXERCISE 4:")
inventory.append("envelope")
print("After append:", inventory)

inventory.remove("tape")
print("After remove:", inventory)

inventory.sort()
print("After sort:", inventory)
print("-" * 30)

# EXERCISE 5 · Intermediate: Tuple comparison
print("EXERCISE 5:")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("Caught expected TypeError:", e)
    print("Tuples are immutable, making them ideal for fixed reference data like GPS coordinates.")
print("Original coords:", coords)
print("-" * 30)

# EXERCISE 6 · Intermediate: Average of a list of sales
print("EXERCISE 6:")
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")
print("-" * 30)

# EXERCISE 7 · Intermediate: Accumulator pattern
print("EXERCISE 7:")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)
print("-" * 30)

# EXERCISE 8 · Advanced: Filter above threshold
print("EXERCISE 8:")
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales_data:
    if s > 300:
        high_sales.append(s)

high_count = len(high_sales)
high_avg = sum(high_sales) / high_count

print("High sales (>300):", high_sales)
print(f"Count: {high_count} | Avg: {high_avg:.2f}")
