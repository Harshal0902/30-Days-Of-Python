
# Variables in Python

first_name = 'Harshal'
last_name = 'Raikwar'
country = 'India'
city = 'Banglore'
age = 19
skills = ['Python','JavaScript','HTML', 'CSS', 'JS', 'React']
person_info = {
    'firstname':'Harshal', 
    'lastname':'Raikwar', 
    'country':'India',
    'city':'Banglore'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age = 'Harshal', 'Raikwar', 'India', 19

print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)