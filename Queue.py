# A queue is a linear data structure that follows the FIFO (First In, First Out) principle. This means the first element added is the first one to be removed.

# Example 01: Ticket Counter Queue

print("(Ticket Queue)")
print("---------------")
ticketQueue = []

ticketQueue.append("Rizjie")
ticketQueue.append("Prince")
ticketQueue.append("Renzo")
ticketQueue.append("Dan")


print("\nNow Serving:", ticketQueue.pop(0))
print("Now Serving:", ticketQueue.pop(0))
print("Now Serving:", ticketQueue.pop(0))
print("Now Serving:", ticketQueue.pop(0))
print("---------------")


# Example 02: Food Order Queue

print("\n(Food Order Queue)")
print("---------------")
foodQueue = []

foodQueue.append("Burger")
foodQueue.append("Pizza")
foodQueue.append("Pasta")
foodQueue.append("Fries")

print("\nPreparing Order:", foodQueue.pop(0))
print("Preparing Order:", foodQueue.pop(0))
print("Preparing Order:", foodQueue.pop(0))
print("Preparing Order:", foodQueue.pop(0))
print("---------------")
