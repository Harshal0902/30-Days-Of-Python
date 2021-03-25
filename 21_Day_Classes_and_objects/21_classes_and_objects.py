# Creating a Class
# syntax
# class ClassName:
#   code goes here
class Person:
  pass


# Creating an Object
p = Person()
print(p)


# Class Constructor
class Person:
      def __init__ (self, name):
          self.name =name

p = Person('Harshal')
print(p.name)
print(p)


# Object Methods
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Harshal', 'Raikwar', 19, 'Bangalore', 'India')
print(p.person_info())


# Object Default Methods
class Person:
      def __init__(self, firstname='Harshal', lastname='Raikwar', age=19, country='India', city='Bangalore'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 19, 'Nomanland', 'Noman city')
print(p2.person_info())


# Method to Modify Class Default Values
class Person:
      def __init__(self, firstname='Harshal', lastname='Raikwar', age=19, country='India', city='Bangalore'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)


# Inheritance
class Student(Person):
    pass


s1 = Student('Eyob', 'Raikwar', 30, 'India', 'Bangalore')
s2 = Student('Lidiya', 'Teklemariam', 28, 'India', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


# Overriding parent method
class Student(Person):
    def __init__ (self, firstname='Harshal', lastname='Raikwar',age=19, country='India', city='Bangalore', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Harshal', 'Raikwar', 19, 'India', 'Bangalore','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
