# 1. Create a list of initial product SKUs (mutable, ordered)
inventory = ["stapler", "notebook", "pen", "tape", "marker"]
print("Initial Inventory:", inventory)

# 2. Add a new item to the end using .append()
inventory.append("envelope")
print("After adding shipment:", inventory)

# 3. Remove a discontinued item using .remove()
inventory.remove("tape")
print("After removing discontinued SKU:", inventory)

# 4. Sort the inventory list in place using .sort()
inventory.sort()
print("Sorted Warehouse Inventory:", inventory)

# 5. Extract top SKUs using slicing
top_items = inventory[:2]
print("Top two items (slice):", top_items)

# 6. Count total active SKUs using len()
print(f"Total Active SKUs: {len(inventory)}")

# 7. Create an immutable Tuple for fixed reference data (e.g., store coordinates)
store_location = (27.9506, -82.4572)  # (Latitude, Longitude)
print("Store Coordinates (Tuple):", store_location)
print(f"Tuple length: {len(store_location)}")
