# Random notes and memory helpers from the Python for Data Science Training

s = "sample text"
word_lst = s.split() #Use split() to split up space delimited words.

# Removing whitespace
s = "\t     something goes here     \n"
s.strip() # removes extra padding around string"

# Chain commands together to split everything into a list w/ 3 elements
s.strip().split()
print("['something', 'goes', 'here']")

# Lists
a = [1, 123, 13, 15]
# append to an existing list
a.append(13) 
# extend another list to existing list
a.extend([3, 6, 19]) 
# remove item at index = n (3 here) with pop
a.pop(3) #
# Insert a new item in index 3
a.insert(3, 100)
# Count occurences of a number/letter in a list
a.count(1)
# Return where the first value of 123 occurs
a.index(123)


# Use tuples for many things (returning multiple values)

# Dictionaries are really useful
# dictionary keys are immutable; store key/value pairs
