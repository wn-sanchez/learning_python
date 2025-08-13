#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

smallest=None
largest=None
while True:
    number= input('Enter number:')
    try:
        n=int(number) 
    except:
        if number=='done':
            print('small: ', smallest, 'big: ', largest)
            break
        else:
            print('error')
            continue

    if smallest is None:
        smallest = n
    elif smallest > n:
        smallest = n
        

    if largest is None:
        largest = n
    elif largest < n:
        largest = n
        continue
    
    
