# Stack is a linear data structure that follows the LIFO (Last In, First Out) principle.

# Example 01: Removing last added items in a shopping cart

print("(Shopping Cart)")
print("---------------")
shoppingCart = []
shoppingCart.append("Laptop")
shoppingCart.append("Wireless Mouse")

print("Removed from Cart:", shoppingCart.pop())
print("Removed from Cart:", shoppingCart.pop())
print("---------------")

# Example 02: Browser Tab Navigation

print("\n(Browser Tab)")
print("---------------")
tabs = []
tabs.append("Google.com")
tabs.append("Facebook.com")
tabs.append("Instagram.com")

print("Back to:", tabs.pop())
print("Back to:", tabs.pop())
print("Back to:", tabs.pop())
print("---------------")