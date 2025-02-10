# A linked list is a linear data structure where elements (nodes) are connected using pointers.

# Example 01: Favorite Movies

class Node:
    def __init__(self, movie):
        self.movie = movie
        self.next = None

movie1 = Node("Lone Survivor")
movie2 = Node("Interstellar")
movie3 = Node("American Sniper")
movie4 = Node("God Of War")
movie5 = Node("!2 Strongholds")

movie1.next = movie2
movie2.next = movie3
movie3.next = movie4
movie4.next = movie5

print("\nFavorite Movies List:")
print("---------------")
current = movie1
while current: 
    print(current.movie, end=" -> ")
    current = current.next
print("End of Favorite Movie List")
print("---------------")

# Example 02: Recent Chats

class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None

chat1 = Node("Rizjie")
chat2 = Node("Prince")
chat3 = Node("Charles")
chat4 = Node("Renzo")

chat1.next = chat2
chat2.next = chat3
chat3.next = chat4

print("\nRecent Chats:")
print("---------------")
current = chat1
while current:
    print(current.contact, end=" -> ")
    current = current.next
print("First Contact")
print("---------------")
