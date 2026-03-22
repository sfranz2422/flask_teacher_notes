"""
A simple web application.
"""
# WARNING START: do not change the following two lines of code.
from flask import Flask, render_template

app = Flask(__name__)
# WARNING END: do not change the previous two lines of code.



#have kids make a web design 2 project folder with a folder named notes inside.  make a templates
# folder inside the notes folder.
# open mu and add third party libraries. save the file as app.py inside the notes folder.


# talk about routes and returning strings.

@app.route("/")
def name_me_anything():

    return "This is going to the web page!"

#2
@app.route("/variables")
def variables():

    name = "franz"

    return name


#3 Numbers
# we can only return strings.
@app.route("/numbers")
def numbers():

    num1 = 5
    num2 = 3
    sum = num1 + num2
    sum = str(sum)
    num1 = str(num1)
    num2 = str(num2)

    return "The sum of " + num1 + " and " + num2 + " is " + sum



 # Activity:
# create a new folder in your webdesign 2 folder named string practice
# make a templates folder inside of the string practice folder
# open mu and start a new flask project
# save the file as app.py in the string practice folder you just created.  Do NOT save in the templates folder.
# in the home route. create 2 variables named num1 and num2.  Assign the value of 10 to num1 and 2 to the value of num2
# Compute the product of num1 and num2 and save the value in a variable called product.
# return the string to the webpage "The product of num1 and num2 is product"  Use the string append operator + to insert the variables into the string.


#4
# we a better way to format strings sring interpolation.
@app.route("/better_strings")
def better_strings():

    name = "franz"

    greeting = f"Nice to meet you {name}"


    return greeting



#5
#
@app.route("/better_formatting")
def better_formatting():
    name = "franz"

    big_string = f"""

    Hello, {name} this ia a big string.

    <br>

    I can even put <em>variables</em> into this <h1>big</h1> string.

    """


    return big_string



 # 6 Activity:
# create a new folder in your webdesign 2 folder named string interpolation
# make a templates folder inside of the string interpolation folder
# open mu and start a new flask project
# save the file as app.py in the string interpolation folder you just created.  Do NOT save in the templates folder.
# create the following variables and give appropriate values.
# holiday
# name1
# verb1
# store
# noun1
# adjective1
# noun2
# adjective2
# noun3
# adjective3
# noun4
# name2
# verb2
# verb3
# adjective4
# type_of_store
# use the following string and string interpolation to fill in the blanks.  Give the string an appropriate
# <h1> heading
# It was almost {holiday}
# , so 'name1'
#  knew they had to get grocery shopping. They 'verb1'
#  to the 'store'
#  and picked up a 'noun1'
# . They looked at their list. They needed to get 'adjective1'
#  'noun2'
# , 'adjective2'
#  'noun3'
# , and 'adjective3'
#  'noun4'
# . They couldn't find anything! Eventually they saw their friend, 'name2'
# , and 'verb2'
#  them for help. Their friend 'verb3'
# . "You're in the 'adjective4'
#  place!" they said. "This is a 'type_of_store'
# store"



#Quiz



#6
# passing arguments in the url
@app.route("/passing_variables/<name>")
def passing_variables(name):

    big_string = f"""

    Hello, {name} this ia a big string.

    <br>

    I can even put <em>variables</em> into this <h1>big</h1> string.

    """


    return big_string






#7
# passing multiple arguments in the url
@app.route("/passing_mult_variables/<name>/<greeting>")
def passing_mult_variables(name, greeting):

    big_string = f"""

    Hello, {name} {greeting}.


    """


    return big_string


#8 lesson on conditionals
@app.route("/conditionals")
def conditionals():

    string1 = "Franz"
    string2 = "franz"
    num1 = 10
    num2 = 5


    # the double equal is called an equality operator ==
    # to test if two values are true.

    print(string1 == string2)
    print(string1 != string2)

    inequality = num1 >= num2
#     return str(string1 != string2)
    return str(inequality)


#9 if lesson
@app.route("/if_statement")
def if_statement():

    string1 = "Franz"
    string2 = "Franz"

    statement = ""

    if string1 == string2:
        statement = "These are equal"


    return statement


#9 if else lesson
@app.route("/if_else_statement")
def if_else_statement():

    string1 = "Franz"
    string2 = "franz"

    statement = ""

    if string1 == string2:
        statement = "These are equal"
    else:
        statement = "These are NOT equal"


    return statement


#9 if lesson with url arguments
@app.route("/argument_conditionals/<string1>/<string2>")
def argument_conditionals(string1,string2):


    statement = ""

    if string1 == string2:
        statement = "These are equal"
    else:
        statement = "These are <span style='color:red;'>NOT</span> equal"


    return statement



# casing arguments
@app.route("/casing_arguments/<int:num1>/<int:num2>")
#There cannot be a space between the colon and the variable name!!
def casing_arguments(num1, num2):
    if num1 > num2:
        statement = f"{num1} is bigger than {num2}"

    else:
        statement = f"{num1} is smaller than {num2}"


    return statement



@app.route("/else_if/<int:num1>/<int:num2>")
#There cannot be a space between the colon and the variable name!!
def else_if(num1, num2):
    if num1 > num2:
        statement = f"{num1} is bigger than {num2}"

    elif num1 < num2 :
        statement = f"{num1} is smaller than {num2}"

    else:
        statement =  f"{num1} is equal to {num2}"

    return statement



#10 pictures
@app.route("/argument_conditionals_pictures/<string1>/<string2>")
def argument_conditionals_pictures(string1,string2):


    statement = ""

    if string1 == string2:
        statement = f"{string1} and {string2} are Equal!"
    else:
        statement = f"""

        {string1} and {string2} are <span style='color:red;'>NOT</span> equal
        <br>
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4f/ISO_7010_P001.svg">

        """


    return statement


#random numbers
# goes at the top of the page
import random
@app.route("/random_number")
def random_number():

    random_number = random.randint(0, 9)
    print(random_number)

    return str(random_number)



#11 Assignment
# see webpage for assignment




