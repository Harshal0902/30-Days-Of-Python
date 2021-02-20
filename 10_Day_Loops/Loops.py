# While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)  # 0 1 2 3 4 5


# Break: We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break  # 0 1 2


# Continue: With the continue statement we can stop the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1  # 0 1 2


# For Loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)  # 0 1 2 3 4 5


# For loop with tuple
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)  # 0 1 2 3 4 5


# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)  # Apple Amazon Oracle Google Facebook Microsoft IBM


# The Range Function
for number in range(11):
    print(number)   # prints 0 to 10, not including 11


# Nested For Loop
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)  # JavaScript React Node MongoDB Python


# For Else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)  # 0 1 2 3 4 5 6 7 8 9 10 The loop stops at 10


# Pass: In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass
