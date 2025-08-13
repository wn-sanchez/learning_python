#Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

fruit = 'banana'
length = len(fruit)
index = length - 1

while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1

#Each time through the loop, the next character in the string is assigned to the variable letter. The loop continues until no characters are left.

fruit = 'banana'
for letter in fruit:
    print(letter)
    
# Using reversed() directly on the string

fruit = 'banana'
for letter in reversed(fruit):
    print(letter)
    