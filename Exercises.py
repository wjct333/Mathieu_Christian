
# Welcome to the Week 7 CodeBench exercise set. As with the Week 6 set, we start with some revision exercises, and then have some slightly longer algorithm design questions to finish.
#
# The code below defines a Person class. Each person has a name and a list of friends that other pople can be added to.
#
# You jobs are to:
#
# Implement the constructor for person so that the name given to the constructor is stored in a member variable called name and a member variable called friends is initialised to an empty list.
#
# Implement the method is_friends_with. If a and b are people then this method should return true if a has been added as a friend of b or if b has been added as a friend of a.
#
# Implement the add_friend method. If a and b are instances of Person then after a.add_friend(b) is called a must be a friend of b and b must be a friend of a.
#
# The tests at the end of the program will check whether all the above conditions are properly implemented by your code.
#
# An exercise on Classes, lecture 12.


# class Person:
#
#     def __init__(self, name):
#         """Create a new person with the given name and no friends."""
#
#     # TODO: Implement this
#
#     def add_friend(self, other):
#         """Make this person and the given other person friends."""
#
#     # TODO: Implement this.
#
#     def is_friends_with(self, other):
#         """Returns True if and only if other is a friend of this person."""
#         # TODO: Fix this
#         return False
#
#
# # DO NOT MODIFY CODE BELOW THIS LINE
# import unittest
#
#
# class FriendTests(unittest.TestCase):
#
#     def test_init(self):
#         alice = Person('Alice')
#         self.assertEqual(alice.name, 'Alice')
#         self.assertEqual(alice.friends, [])
#
#     def test_add(self):
#         alice = Person('Alice')
#         bob = Person('Bob')
# #         alice.add_friend(bob)
# #         self.assertTrue(alice.is_friends_with(bob))
# #         self.assertTrue(bob.is_friends_with(alice))
#
# # Q3 Classes are a useful way of storing related data items (in much the same way that a dictionary can store key-value pairs).
# # The code in this exercise implements a class for holding name and email address information.
# # The function extract_names operates on a list of Contact objects to extract the names and return them in sorted order.

class Contact:
    """Encapsulates an email contact."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

# # DO NOT MODIFY CODE ABOVE THIS LINE

def extract_names(address_book):
    """Return a sorted list of all names in an address book,
    implemented as a list of Contact objects."""

    names = []
    for contact in addr_book:
        names.append(contact.name)
    return sorted(names)

    # TODO: implement this function and replace the return statement


# DO NOT MODIFY CODE BELOW THIS LINE

addr_book = []
addr_book.append(Contact("Mickey Mouse", "mickey@disneyland.com"))
addr_book.append(Contact("Minnie Mouse", "minnie@disneyland.com"))
addr_book.append(Contact("Goofy", "goofy@disneyland.com"))
addr_book.append(Contact("Pluto", "pluto@disneyland.com"))
addr_book.append(Contact("Winnie the Pooh", "poohbear@disneyland.com"))

print("\n".join(extract_names(addr_book)))



