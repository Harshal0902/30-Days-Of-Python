# Setting up your project directory
#pip install virtualenv


# Creating routes
# Home routes
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


# Let's add additional route. Creating about route
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


# Creating templates
# home.html
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Home</title>
#   </head>

#   <body>
#     <h1>Welcome Home</h1>
#   </body>
# </html>

# about.html
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>About</title>
#   </head>

#   <body>
#     <h1>About Us</h1>
#   </body>
# </html>


# Python Script
# app.py

# # let's import the flask
# from flask import Flask, render_template
# import os # importing operating system module

# app = Flask(__name__)

# @app.route('/') # this decorator create the home route
# def home ():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# if __name__ == '__main__':
#     # for deployment we use the environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# Navigation
# <ul>
#   <li><a href="/">Home</a></li>
#   <li><a href="/about">About</a></li>
# </ul>


# # let's import the flask
# from flask import Flask, render_template, request, redirect, url_for
# import os # importing operating system module

# app = Flask(__name__)

# @app.route('/') # this decorator create the home route
# def home ():
#     techs = ['HTML', 'CSS', 'Flask', 'Python']
#     name = '30 Days Of Python Programming'
#     return render_template('home.html', techs=techs, name = name, title = 'Home')

# @app.route('/about')
# def about():
#     name = '30 Days Of Python Programming'
#     return render_template('about.html', name = name, title = 'About Us')

# @app.route('/post')
# def post():
#     name = 'Text Analyzer'
#     return render_template('post.html', name = name, title = name)


# if __name__ == '__main__':
#     # for deployment
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)


# home.html
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Home</title>
#   </head>
#   <body>
#     <ul>
#       <li><a href="/">Home</a></li>
#       <li><a href="/about">About</a></li>
#     </ul>
#     <h1>Welcome to {{name}}</h1>
#     {% for tech in techs %}
#     <ul>
#       <li>{{tech}}</li>
#     </ul>
#     {% endfor %}
#   </body>
# </html>

# about.html
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>About Us</title>
#   </head>
#   <body>
#     <ul>
#       <li><a href="/">Home</a></li>
#       <li><a href="/about">About</a></li>
#     </ul>
#     <h1>About Us</h1>
#     <h2>{{name}}</h2>
#   </body>
# </html>


# layout.html
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <link
#       href="https://fonts.googleapis.com/css?family=Lato:300,400|Nunito:300,400|Raleway:300,400,500&display=swap"
#       rel="stylesheet"
#     />
#     <link
#       rel="stylesheet"
#       href="{{ url_for('static', filename='css/main.css') }}"
#     />
#     {% if title %}
#     <title>30 Days of Python - {{ title}}</title>
#     {% else %}
#     <title>30 Days of Python</title>
#     {% endif %}
#   </head>
#   <body>
#     <header>
#       <div class="menu-container">
#         <div>
#           <a class="brand-name nav-link" href="/">30DaysOfPython</a>
#         </div>
#         <ul class="nav-lists">
#           <li class="nav-list">
#             <a class="nav-link active" href="{{ url_for('home') }}">Home</a>
#           </li>
#           <li class="nav-list">
#             <a class="nav-link active" href="{{ url_for('about') }}">About</a>
#           </li>
#           <li class="nav-list">
#             <a class="nav-link active" href="{{ url_for('post') }}"
#               >Text Analyzer</a
#             >
#           </li>
#         </ul>
#       </div>
#     </header>
#     <main>
#       {% block content %} {% endblock %}
#     </main>
#   </body>
# </html>


# about.html
# {% extends 'layout.html' %} {% block content %}
# <div class="container">
#   <h1>About {{name}}</h1>
#   <p>
#     This is a 30 days of python programming challenge. If you have been coding
#     this far, you are awesome. Congratulations for the job well done!
#   </p>
# </div>
# {% endblock %}

# post.html
# {% extends 'layout.html' %} {% block content %}
# <div class="container">
#   <h1>Text Analyzer</h1>
#   <form action="https://thirtydaysofpython-v1.herokuapp.com/post" method="POST">
#     <div>
#       <textarea rows="25" name="content" autofocus></textarea>
#     </div>
#     <div>
#       <input type="submit" class="btn" value="Process Text" />
#     </div>
#   </form>
# </div>
# {% endblock %}


# # let's import the flask
# from flask import Flask, render_template, request, redirect, url_for
# import os # importing operating system module

# app = Flask(__name__)
# # to stop caching static file
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



# @app.route('/') # this decorator create the home route
# def home ():
#     techs = ['HTML', 'CSS', 'Flask', 'Python']
#     name = '30 Days Of Python Programming'
#     return render_template('home.html', techs=techs, name = name, title = 'Home')

# @app.route('/about')
# def about():
#     name = '30 Days Of Python Programming'
#     return render_template('about.html', name = name, title = 'About Us')

# @app.route('/result')
# def result():
#     return render_template('result.html')

# @app.route('/post', methods= ['GET','POST'])
# def post():
#     name = 'Text Analyzer'
#     if request.method == 'GET':
#          return render_template('post.html', name = name, title = name)
#     if request.method =='POST':
#         content = request.form['content']
#         print(content)
#         return redirect(url_for('result'))

# if __name__ == '__main__':
#     # for deployment
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)