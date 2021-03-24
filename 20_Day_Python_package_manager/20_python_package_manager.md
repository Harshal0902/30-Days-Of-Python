## Python PIP - Python Package Manager

### Installing PIP

If you did not install pip, let us do it now. Go to your terminal or command prompt and copy and paste this:

```sh
harsh@harsh:~$ pip install pip
```

Check if it is installed by writing

```sh
pip --version
```

```py
harsh@harsh:~$ pip --version
pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```


### Installing packages using pip

Let's try to install _numpy_, called numeric python. It is one of the most popular packages in machine learning and data science community.


```sh
harsh@harsh:~$ pip install numpy
```

Lets start using numpy. Open your python interactive shell, write python and then import numpy as follows:

```py
harsh@harsh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.17.3'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>
```

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Let's install the big brother of numpy, _pandas_:

```sh
harsh@harsh:~$ pip install pandas
```

```py
harsh@harsh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

This section is not about numpy nor pandas, here we are trying to learn how to install packages and how to import them. If it is needed, we will talk about different packages in other sections.

Let's import a web browser module, which can help us to open any website. We do not install this module, it is already installed by default with python 3. For instance if you like to open any number of websites at any time or if you like to schedule something, this _webbrowser_ module can be of use.

```py
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/harshal/',
    'https://twitter.com/harshalraikwar6',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Uninstalling Packages

If you do not like to keep the installed packages, you can remove them.

```sh
pip uninstall packagename
```

### List of Packages

To see the installed packages on our machine. We can use pip followed by list.

```sh
pip list
```

### Show Package

To show information about a package

```sh
pip show packagename
```

```sh
harsh@harsh:~$ pip show pandas
Name: pandas
Version: 0.25.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

If we want even more details, just add --verbose

```sh
harsh@harsh:~$ pip show --verbose pandas
Name: pandas
Version: 0.25.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

Generate output suitable for a requirements file.

```sh
harsh@harsh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

### Reading from URL

By now you are familiar with how to read or write on a file located on you local machine. Sometimes, we would like to read from a website using url or from an API.
API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. To open a network connection, we need a package called _requests_ - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading part of a CRUD.

Let's install _requests_:

```py
harsh@harsh:~$ pip install requests
```

We will see _get_, _status_code_, _headers_, _text_ and _json_ methods in _requests_ module:
  - _get()_: to open a network and fetch data from url - it returns a response object
  - _status_code_: After we fetched data, we can check the status of the operation (succes, error, etc)
  - _headers_: To check the header types
  - _text_: to extract the text from the fetched response object 
  - _json_: to extract json data
Let's read a txt file form this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
```

### Creating a Package

We organize a large number of files in different folders and subfolders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. Let's create a package named mypackage, using the following steps:

Create a new folder named mypacakge inside 30DaysOfPython folder
Create an empty **init**.py file in the mypackage folder.
Create modules arithmetic.py and greet.py with following code:

```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

The folder structure of your package should look like this:

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```
