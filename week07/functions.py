# ==============================================================================
# SELF-ASSESSMENT & DISCLOSURE
# Q1: How do functions improve code reusability and organization?
# Answer: Functions encapsulate blocks of logic so they can be written once and 
# called multiple times with different inputs, reducing code duplication.
#
# Q2: What is the difference between local and global scope?
# Answer: Global variables are defined outside functions and accessible 
# everywhere, whereas local variables are created inside functions and 
# only exist within that specific function's scope.

# ==============================================================================


# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

t1 = calculate_tax(100, 0.07)
t2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${t1:.2f}")
print(f"Tax on $250 at 8%: ${t2:.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)

base_price = 200.0
for t in ["gold", "silver", "bronze", "none"]:
    res = apply_discount(base_price, t)
    print(f"{t}: ${res:.2f}")


# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount

starting_price = 200
gold_price = apply_discount(starting_price, "gold")
with_tax = final_price(starting_price, "gold", 0.07)
print(f"After gold discount: ${gold_price:.2f}")
print(f"After tax: ${with_tax:.2f}")
print(f'final_price(200, "gold", 0.07) = ${with_tax:.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 6 ---
x = 100  # global variable

def double_it():
    x = 999  # local variable — different from global x!
    return x * 2

print(x)           # prints 100
print(double_it()) # prints 1998
print(x)           # prints 100

# Scope Explanation:
# Variables created inside a function are local to that function. 
# Changing 'x' inside double_it() only changes the local 'x', so the global 'x' outside stays 100.
