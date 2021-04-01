# Installation
# pip install conda
# pip install pandas


# Importing Pandas
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np


# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64


# Creating Pandas Series with custom index
fruits = ['Orange','Banana','Mangao']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
# 1    Orange
# 2    Banana
# 3    Mangao
# dtype: object


# Creating Pandas Series from a Dictionary
dct = {'name':'Harshal','country':'India','city':'Bangalore'}
s = pd.Series(dct)
print(s)
# name       Harshal
# country     India
# city       Bangalore
# dtype: object


# Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2,3])
print(s)
# 1    10
# 2    10
# 3    10
# dtype: int64


# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)
# 0     5.000000
# 1     6.666667
# 2     8.333333
# 3    10.000000
# 4    11.666667
# 5    13.333333
# 6    15.000000
# 7    16.666667
# 8    18.333333
# 9    20.000000
# dtype: float64


# Creating DataFrames from List of Lists
data = [
    ['Harshal', 'India', 'Bangalore'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)


# Creating DataFrame Using Dictionary
data = {'Name': ['Harshal', 'David', 'John'], 'Country':[
    'India', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)


# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Harshal', 'Country': 'India', 'City': 'Bangalore'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)


# Reading CSV File Using Pandas
import pandas as pd
df = pd.read_csv('weight-height.csv')
print(df)


# Creating a DataFrame
import pandas as pd
import numpy as np
data = [
    {"Name": "Harshal", "Country":"India","City":"Bangalore"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)


# Adding a New Column
weights = [74, 78, 69]
df['Weight'] = weights
df


# Let's add a height column into the DataFrame aswell
heights = [173, 175, 169]
df['Height'] = heights
print(df)


# Modifying column values
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()


# Formating DataFrame columns
df['BMI'] = round(df['BMI'], 1)
print(df)
