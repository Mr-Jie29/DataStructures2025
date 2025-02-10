# An array is a data structure that stores multiple values of the same data type in a continuous memory location. Each value (element) is accessed using an index.

# Example 01: Student Marks
print("(Student Marks)")
print("---------------")
marks = [99, 100, 75]
print("Highest Mark:", max(marks))

marks.append(98)
marks.remove(75)

print("Updated Marks:", marks)
print("---------------")

# Example 02: Car Dealer 

print("\n(Car Dealer)")
print("---------------")
cars = ["Toyota Supra", "Ford Mustang", "Chevrolet Camaro"]
print("Sold Car:", cars[1])

cars.append("Dodge Charger")
cars.remove("Ford Mustang")

print("Updated Car For Sale:", cars)
print("---------------")
