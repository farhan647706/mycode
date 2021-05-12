#!/usr/bin/env python3

message = 'The movie is about to begin, we recommend '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("Select you movie "))

# if input value was higher or equal to 4
if connection == 1:
    message = message +  'Harry Potter.'
elif connection == 2:
    message = message + 'Hobbit & Lord of the Rings'
elif connection == 3:
    message = message + 'Chronicles of Narnia'
else:
    message = 'Sorry! selection is not available'
print(message)

