"""
 demo.py
 Simple Python scripts to demonstrate print statements
  and basic arithmetic operations.
"""


"""
 demo.py
 Simple Python scripts to demonstrate print statements
  and basic arithmetic operations.
"""


"""
print("Welcome to the python world !!!", 
      "This is my first demo script.",
    "Python is fun to learn and use.", "Happy coding!", 
        "Let's explore more Python features.")

#  Time for some arithmetic operations using python.
#  Addition, Subtraction, Multiplication, Division, 
# ... Integer Division, Modulus, Exponentiation
print("This is to print some arithmetics using python. ")
print("21+4= ", 21+4)
print("Multiplication: 7*6= ", 7*6)
print("Division: 56/8= ", 56/8)
print("Subtraction: 45-9= ", 45-9)
print("Integer Division: 22//7= ", 22//7)
print("Modulus: 29%5= ", 29%5)
print("Exponentiation: 3**2= ", 3**2)
print("That's all for now. More to come soon...")
"""


"""
print("Welcome to the python world !!!", 
      "This is my first demo script.",
    "Python is fun to learn and use.", "Happy coding!", 
        "Let's explore more Python features.")

#  Time for some arithmetic operations using python.
#  Addition, Subtraction, Multiplication, Division, 
# ... Integer Division, Modulus, Exponentiation
print("This is to print some arithmetics using python. ")
print("21+4= ", 21+4)
print("Multiplication: 7*6= ", 7*6)
print("Division: 56/8= ", 56/8)
print("Subtraction: 45-9= ", 45-9)
print("Integer Division: 22//7= ", 22//7)
print("Modulus: 29%5= ", 29%5)
print("Exponentiation: 3**2= ", 3**2)
print("That's all for now. More to come soon...\n")
print()
"""

"""
#...Some BODMAS rules.
print("Let's try some BODMAS rules now...")
print()
ba= (8*(25/5)-2)
print(ba, "\n")
ab= (30/5)*(22-6)/4
print(ab)
"""

"""
#...Now time for Data types
name = "Sanaullah"
age = 25
height = 5.4
is_student = True
skills = ["Python", "Data Analysis", "SQL"]
"""

"""
#...This prints the type of the data.
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(skills))
"""

print()
#...This print() is used for a line break.

"""
#...String concatenation and Replication.
print('Zerak ' + 'Khan')
print('Zerak' + "24", "\n")

'''This will result in a error.
Because we can't combine 
string values to an integer directly.'''

print('Zerak Khan  '*5)
'''This returns Zerak Khan 5 times.'''
print()
"""

"""
#...Storing Values in Variables.
spam= 40
print(spam)

eggs= 2
print(spam+eggs+spam)

spam= spam +2
print(spam)

var= 233
print(var +2, "\n")
print("\n")
"""

'''
The first program
'''

'''
 #...This program says and asks for my name.
print("Hello world!")
print("What's your name ?") # Ask for their name.
myName= input()
print("It's good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName),"\n")
print("What's your age ?") # Ask for their age.
myAge= float(input())
print(f"You will be {myAge + 1} in a year.\n")
print()
'''
print()
"""
name = "Sanaullah"
print(f"My name is {name}")
print()

pi= round(3.14159)
print(pi)
print(type(pi))
"""



#...Boolean Logic in python.
"""
print(45 == 45.0)
print(34 == '34')

print("True and false statements in python."
      "== checks whether values are same.")
a= [1,2,3,4]
b= [1,2,3,4]
print(a==b,"\n")

print(90 == 0090.00,"\n")

bacon= 20
print(bacon + 1)
print(bacon)

print('spam' + 'spamspam')
print('spam' * 3)
print()

total_burritos= 99
print('I have eaten ' + str(total_burritos) +
       ' burritos.')
print()


#...Boolean values, comparison operators, and Boolean operators.
spam= True
print(spam)
print(34 == 23)
print(2 != 3)
print(2!= 2)
print()
"""


#...Comparison operators
"""
eggcount= 42
print(eggcount <= 42)
myage= 26
print(myage >= 10)
print()
"""



###...Boolean operators...###
"""
#..AND operator
print(True and True) #..AND operator evaluates to TRUE only when both of its operands are True.
print(True and False)
print(False and True)
print(False and False)
print()

#..OR operator
print(True or True)
print(True or False)
print(False or True)
print(False or False)  #..OR operator returns false value only when both are false.
print()
"""

"""
#..Mixing Operators
print(not True)
print((not False) and True)
print((not False) or False)
print((not True) or False)
print(True or False)
print(False and True)
print(True and False)

print(not True)
print(not False)
print() 
"""


#...Mixing Boolean and Comparison Operators
'''
print((4 < 5) and (5 < 6))
print((4 < 5) or (9 < 6))
print((1 == 2) or (2 == 1))
print()

print('dog' != 'cat')
print('dog' == 'cat')
print()


print("What is your name ?")
name= input()
if name == 'Alice':
  print(f"It's good to meet you, {name}.")
print()
'''


'''
print('What is your name?')
nam= input()
if nam == 'Alice':
  print(f'Nice to meet you, {nam}')
else:
  print('Hello, stranger.')
print()
'''

'''
print('What is your name ?')
nom= input()
print(f'What is your age ?')
sokalan= float(input())

if nom== 'Sanaullah Khan' and sokalan== 26:
  print(f'Welcome, Sir',nom)
elif sokalan < 26:
  print('You are not him. kiddo')
elif sokalan == 26:
  print('Welcome, Sir')
'''
  
'''
pswd = "swordfish"
print('Type password')
pswd= input()
print()

if pswd == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password !')
'''

'''
#...elif examples.
print('What is your name ?')
name= input()
print()
print('How old are you ?')
age= int(input())

if name != 'Alice':
    print('Unauthorized access denied!.')
elif name == 'Alice' and age == 12:
    print('Hi Alice.')
elif age < 12:
    print('Have you done your homework ?',"Get off the PC 😖. Right now!!!")
elif age > 49:
    print("You're nor Alice granny.")
elif 49 < age < 125:
    print('You are definitly not Alice. Kindly turn the PC off!')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
else:
    print('You are not Alice at all...')
'''

'''
#...Nested statements.
print('What is your name ?')
name= input()

if name != 'Alice':
    print('Access denied!')
else:
  print('How old are you ?')
  age= int(input())
  print()

  if name != 'Alice':
      print('You are not Alice at all.')
  elif name == 'Alice' and age == 12:
      print('Hi Alice, please enter your password')
  elif age < 12:
      print('Have you done your homework ?',"Turn off the PC. Right now!!!")
  elif age > 49:
      print("You're not Alice granny.")
  elif 12 < age < 49:
      print('Access denied!\nYou are not an authorized person.')
  elif age > 2000:
      print('Unlike you, Alice is not an undead, immortal vampire.')
'''

'''
###...Use of Truthy and Falsy values.

print("Enter a name.")
name= input()
if name!= '':
    print("\nThanks for entering a name.")
else:
    print("You didn't enter a name.")
'''

'''
#...Bool function 
# Bool function in python is like a strict judge.
# If you have something (meaningful) entered --> Bool returns True otherwise False.
print(bool(True))
print(bool(False))
print(bool()) #..Bool function returns false, because nothing was entered.
print(bool("")) # Bool function returns because of empty string.
print(bool(''))
print(bool(0.0))
print(bool(0))
print(bool('Hello'))
'''

'''
###...While loop
spam= 0
while spam < 5: #As long as spam<5 the while loop will keep looping.
    print('Hello world!')
    spam = spam + 1

###...If statement
spam= 0
if spam < 5:
    print('Hello World five times using if statemet.')
    spam= spam + 1
'''
"""
name= ''
while name != 'your name':
    print("Please type your name.")
    name= input()
print("Thank you!")
"""

'''
name= ""
while True:
    print("Please type your name.")
    name= input()
    if name== "your name":
        print("Thanks!")
        break
'''

'''
#...continue statements
spam= 0
while spam < 5:
    spam= spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
'''

"""
#...for loop

print("My name is ")
for i in range (0,5):
    print("Sunny 5 times. " + str(i))
"""

"""name= ''
while not name:
    print('Enter your name: ')
    name= input()
print('How many guests will you have ?')
numofGuests= int(input())
if numofGuests:
    print('Be sure to have enough room for all your guests.')
    print('Done')"""


"""print("What is your name five times?: ")
name= str(input())
for nm in range(0,6):
    print(nm, name)
"""


"""
#...Sum of all the numbers from 0 to 100.
total= 0
for i in range(0,101):
    total= total+i
print(total, "\nhahaha... I am clever like Guass.")
"""

"""
Sum= 0
for i in range(0,101):
    Sum= Sum + i
print(Sum)

numbers= (1, 2, 2, 3)
print(numbers[1:3]) # Output: (2, 2)

text = "Python"
print(text[1:4])  # 'yth' → starts at index 1 ('y'), stops before index 4 ('h' included, 'o' excluded)
"""

"""
nums= 0
for i in range(0,20):
    i= i+1
    print(i)
print()
"""


"""
sum= 0
for i in range(0,51):
    sum= sum+i
    print(sum)
"""


"""
print("Enter a number from 1 to 10: ")
num= int(input())
print("\n")
for i in range(1,11):
        print(num, "X", i, "= ", num*i)
"""


"""
#...This program prints all the even numbers between 1 and 100.
for i in range(1,101):
    if i%2 == 0:
        print(i)
"""

"""
#...This program prints all odd numbers between 1 and 100.
for i in range(1,101):
    if i%2 != 0:
        print(i)
"""


"""
#.This program counts the number of vowels in a text.
txt= input("Enter a string: \n")
vcount= 0
for ch in txt:
    if ch.lower() in "aeiou":
        vcount += 1
print(f"The text contains",vcount,"vowels.")
"""

"""
#...This program prints the reverse of any string entered by the user.
rstr= ""
ostr= input("Type a string: \n")
for char in ostr:
    rstr= char + rstr
print(f"The reverse string is: ",rstr)
"""

"""
#...This program returns factorial of a number.
r= 1
num= int(input("Enter a number: "))
for i in range(1, num+1):
    r *= i
print(f"The factorial of",num,"is:",r,".")
"""

"""
#...This program prints a message with each item in the list.

items = ["apple", "banana", "mango", "orange"]
for i in items:
    print(f"I like",i)
"""

"""
x= 0
for i in range(3):
    x += i
print(i,x)
"""

'''
#...The range function.
i= 0
for i in range(0,100,2):
    print(i)
'''

'''
#...Importing modules.
import random

for i in range(12):
    print(random.randint(1,10))


py= "Python"

for letter in py:
    print(letter + "ut")
'''

"""
#...Importing functions from modules.

from random import *
import os
import sys
from math import sqrt
import random
import datetime
import json
import re
import subprocess
from pathlib import Path
from collections import Counter
from typing import List
"""


#...FUNCTIONS
"""
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('HELLO there.')

hello()
"""

#...FUNCTIONS with parameters.
"""
def hello(name):
    print(f"Hello", name)
hello('Alice')

def hello(name):
    name= str(name)
    print("Welcome to python. Mr.",name)
hello('Asif')
hello('Azaz')
hello('Sanaullah')

print("What is your name?")
name= str(input())
def hello(name):
    print("Hello",name)
hello(name)

spam= print("Hello!\n")
print(None== spam)

"""

"""
import random
print(random.randint(1,10))
print(random.randint(10,1))
#This will cause an error,
# because the order of arguments passed to a function matter.
"""


#...break statement in WHILE loop.
'''
wc= 0
while wc < 100:
    wc += 1
    print("Welcome here!",wc)
    if wc == 50:
        break
'''

#...Arguments [To the print function].
"""print("Hello",end= "")
print("World!!!\n")


print("Sanga","yee","?\n",end="",sep=' ') #Custom arguments to the print ftn.
print("That means")
import time
words= ["'","How ","are ", "you ", "?","'"]
for word in words:
    print(word, sep= " ", end= "",flush= True)
    time.sleep(0.5)
print("\nin english.")


string1= "Hello"
string2= "World"

print(string1 + string2)
"""

"""
#...'random' Module.
#..The random module contains functions that help you generate:
# ✔ random numbers
# ✔ random choices from a list
# ✔ shuffled items
# ✔ random Boolean values
# … and more!
import random
print(random.uniform(1,10))

basket= ["red"]*4 + ["blue"]*2
print(random.sample(basket, 4),"\n")

print(random.randint(1,6),"\n")
print(random.uniform(1,100),"\n")
"""

"""
import random
def getanswer(answernumber):
    if answernumber== 1:
        return 'Go back'
    elif answernumber== 2:
        return 'Yes.'
    elif answernumber== 3:
        return 'Why are you running?'
    elif answernumber== 4:
        return 'You are at the right place.'
    elif answernumber== 5:
        return 'You should see this.'
    elif answernumber== 6:
        return 'Ask again later.'
    elif answernumber== 7:
        return 'Concentrate and ask again.'
    elif answernumber== 8:
        return 'Cooporate or get fired.'
    elif answernumber== 9:
        return 'Very doubtful'
r= random.randint(1,9)
fortune= getanswer(r) #The variable fortune is useful because 
# Functions return values; variables remember them (for later re-using).
print(fortune, "\n")

# Shorter version of the above last lines.
print(getanswer(random.randint(1,9)))
"""


#...The call stack (Function stacking) in python.
"""
def a():
    print('a() starts')
    b() #This calls b() function while a() still running.
    d() #This calls d() function while a() still running.
    print('a() returns')
def b():
    print('b() starts')
    c() #This calls c() function while b() still running.
    print('b() returns')
def c(): #c() does'nt call any functions, It just print statements.
    print('c() starts')
    print('c() returns')
def d(): #d() also doesn't call any functions, it just prints statements.
    print('d() starts')
    print('d() returns')

a()  # a() is called. Inside a(), the functions b() and d() are called in order.
     # b() then calls c(), so c() also runs.
"""

#...Local and Global scope in python.
"""
def cotton():
        eggs= 330 #Variable in Local scope.
        print(eggs,"\n")

cotton()
print(eggs) #Local scope variable is called thus it will give NameError.
"""

# Code in local scope can access any variable.
# SHADOWING: We can use same names for global variables and local variables.
#.. In general we should avoide SHADOWING.
"""
eggs= 99 # eggs defined in global scope.

def cotton():
    print(eggs) # egg called in local scope.
cotton()

def spam():
    print(eggs)

eggs= 42 # eggs defined in global scope.
spam()
print(eggs) # egg called in local scope.
"""

"""
eggs= 42

def jam():
    eggs = 10   # local shadowing [Same variable is called inside the ftn as global var.]
    print("Inside jam:", eggs)

jam()
print("Outside:", eggs)
"""

"""
bacon local
spam local
bacon local
global
"""

#...Local and Global Variables with the Same Name
"""
def bacon():
    lc= "bacon local"
    print(lc)
bacon() #prints 'bacon local'

def spam():
    lc= "spam local"
    print(lc)
spam() # prints 'spam local'

lc= "global"
bacon()
print(lc)
"""

#..Line order matters during execution,
#  but scope is decided before execution.
"""
def ftn():
    print(eggs)
    eggs= 'local eggs'

eggs= 'global'
ftn()
"""


#...Exception handeling.
"""
def div(divideby):
    try:
        return 42/divideby
    except:
        print("'Error': Invalid argument.")

print(div(2))
print(div(12))
print(div(0)) #..Division by zero. (ZeroDivisionError)
print(div(1))
"""

# The reason print(div(1)) is never executed is because 
# once the execution jumps to the code in the except clause,
# it does not return to the try clause.
# Instead, it just continues moving down as normal.

"""
def div(divideby):
    return 42/divideby
try:
    print(div(2))
    print(div(12))
    print(div(0))
    print(div(1))
except:
    print("'Error': Invalid argument.")

div(42)
"""

"""
x= 0.1
y= 0.2
print(0.1+0.2== 0.3)

print(0.5 + 0.5== 1)
"""


# Lambda function in python.
#  lambda arguments: expression

# print((lambda a,b: a+b))
"""
add_with_lambda= lambda x,y: x+y
x= float(input("Enter value of x: "))
y= float(input("Enter value of y: "))
result= round(add_with_lambda(x,y),1)
print(result)


name= "Sanaullah"
age= 20
def check_age(age):
    if age > 18:
        return "Adult"
    else:
        return "Minor"        
status= check_age(age)

print("Name:", name)
print("Status:", status)
"""


#...Classes Practice
"""
class Student:
    def __init__(self, name, age, marks, religion, subject, country):
        self.marks= marks
        self.age= age
        self.country= country
        self.religion= religion
        self.name= name
        self.subject= subject
    def show(self):
        print(f"{self.name}, {self.age} y.o has scored {self.marks} in {self.subject}. He is a {self.religion} from {self.country}.")
s1= Student("Ali", 23, 85, "muslim", "Computer Science", "malaysia")
s1.show()


class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    def show(self):
            print(f"{self.name} scored {self.marks}")
class Staff:
    def __init__(self, name, experience, qualification):
        self.name= name
        self.experience= experience
        self.qualification= qualification
    def show(self):
        print(f"{self.name} has {self.experience} of experience and has successfully percieved his {self.qualification}.")
s1= Student("Ali", 85)
stf= Staff("Khan", "8 years", "PhD")
s1.show()
stf.show()
"""

"""
class Spaceship:
   # Class attribute
   tractor_beam = 'off'

   # Instance attributes
   def __init__(self, name, kind):
       self.name = name
       self.kind = kind
       self.speed = None

  # Instance methods
   def warp(self, warp):
       self.speed = warp
       print(f'Warp {warp}, engage!')

   def tractor(self):
       if self.tractor_beam == 'off':
           self.tractor_beam = 'on'
           print('Tractor beam on.')
       else:
           self.tractor_beam = 'off'
           print('Tractor beam off')
class Car:
    wheels= 4
c1= Car()
c2= Car()

c1.wheels= 6

def greeting(name):
    print(f"Wellcome {name} !")
    print(f"{name}! You are part of the team now.")
#..Function call.
greeting("Rebecca")


# Function for the area of a Triangle.
def aot(base, height):
    area= (base*height)/2
    print(f"The area of the given triangle is: {area}.")
    return area
aot(18,2)


#Function for Converting Hour,Minute,Second to Total seconds.
def get_seconds(hours, minutes, seconds):
    ts= 3600*hours+60*minutes+seconds
    return print(f"Total seconds: {ts}")
get_seconds(2,15,34)


# Function for getting a lucky number.
def lucky_num(name):
    num= len(name)*9
    return print(f"Hello {name}. You lucky number is {num}.")
lucky_num("Azaz Khan")


print("Please insert a number.")
a= input();
y= 1
for i in range(int(a)):
    y= y*(i+1)
    print(y)
"""

"""
# This function takes an integer as an input and returns its factorial.
def factorial(n):
    # Exclude 0 as product, start with 1
    y = 1
    for i in range(int(n)):
        y = y*(i+1)
    return y

print(f"Enter a number to get its factorial: ")
input_num= input()
print(f"Factorial of {input_num} is: {factorial(input_num)}")


# Letters that occur earlier in the alphabet evaluate to less than letters from later in the alphabet.
# BOTH sides of an `and` statement must be true to return True.

print("Yellow" > "Cyan" and "Brown" > "Magenta")
print("C" > "A")
print("N" < "M")

# `not` reverses Boolean evaluation of what follows it.
print(not 42 == "Answer")


def check_username(uname):
    if len(uname) < 8:
        print("Invalid username. Must be at least 8 characters long.")
    elif len(uname) >= 8:
        print("Valid username.")
print("Insert username: ")
uname= input(str())
check_username(uname)



# A function that uses modulo to check whether an integer is even or odd.
def is_even(number):
    if int(number) % 2 == 0:
        print("The given integer is even.")
    elif int(number) % 2 != 0:
        print("The given integer is odd.")
    else:
        print("Invalid entry!")
print("Enter a number: ")
intg= int(input())
is_even(intg)


def is_odd(x):
    if x % 2 == 0:
        return "False"
    return "True"
print(is_odd(23))


# Writing the above code using return in the function.
def is_even(number):
    if number % 2 == 0:
        return "The given integer is even."
    elif number % 2 != 0:
        return "The given integer is odd."
    else:
        return "Invalid entry!"
print("Enter an integer: ")
result= int(input())
print(is_even(result))


def total_sales(n):
    revenue= n*7.99
    return revenue
print(total_sales(59))

def total_sales(price, num_tickets):
    result= round(price*num_tickets)
    return result
print(total_sales(7.99, 59))
print(total_sales(15.99, 1001))
"""

"""
def send_email(num_visits, visit_email):
    if num_visits >= visit_email:
        return "Send email."
    else:
        return "Not enough visits."
#print(send_email(5,8))
print(send_email(num_visits=3, visit_email=5))
print(send_email(num_visits= 5, visit_email= 5))
print(send_email(num_visits= 15, visit_email= 10))

def send_email(num_visits, visits_email, visits_coupon):
    if num_visits == visits_email:
        return "Send email only."
    elif num_visits >= visits_coupon:
        return "Send email with coupon."
    elif num_visits < visits_email:
        return "Not enough visits."
    elif num_visits > visits_email or num_visits < visits_coupon:
        return "Send email only."
print(send_email(3,5,8))
print(send_email(5,5,8))
print(send_email(6,5,8))
print(send_email(8,5,8))
print(send_email(10,5,8))

# While loop for counter. 
x= 0
while x < 5:
    print("Not there yet, x= "+ str(x))
    x= x+1
    print("x=" + str(x))
    if x== 5:
        print("There we are!")
    else:
        pass
"""

"""
# Number guessing game in python.
import random

number= random.randint(1,25)
num_guesses= 0

while num_guesses < 5:
    print(f"You have only have {5 - num_guesses} attmepts left.", end= "\n")
    guess= int(input("Enter your guess: "))
    num_guesses += 1

    if guess == number:
        print("Excellent guess!", end= "\n")
    else:
        print("Incorrect guess! Try again.", end= "\n\n")
if guess != number:
    print(f"Game over! The correct number was {number}.", end= "\n")

i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print("Running extra logic")
    i += 1

i= 0
while i<5:
    i += 1
    print(f"Candy perchased: {i}")

i= 0
while i <= 101:
    if i % 10== 0:
        print(f"Candy perchased: {i}")
    i += 1
from time import sleep
mins= 10

while mins > 0:
    print(int(mins))
    sleep(1)
    mins -= 1

    if mins == 5:
        print("Place your reservation soon! 5 minutes remaining.")
    else:
        pass
    if mins == 2:
        print("Don't lose your seats! 2 minutes remaining.")
    else:
        pass
if mins == 0:
  print("User timed out.")
else:
    pass


# Fahrenheit to Celcius.
def to_celsius(x):
    return (5/9)*(x-32)
for x in range(1, 101, 10):
    print(x, to_celsius(x))


score_list= [1,2,3,4,5,6,7,8,9,10]
def score_counter(score_list):
    negative_scores = 0
    neutral_scores = 0
    positive_scores = 0

    for score in score_list:
        if score >= 9:
            positive_scores += 1
        elif score >= 6:
            neutral_scores += 1
        else:
            negative_scores += 1
    print('Negative:', negative_scores)
    print('Neutral:', neutral_scores)
    print('Positive:', positive_scores)
score_counter(score_list)


score_list= [1,2,3,4,5,6,7,8,9,10]
def score_counter():
    bins= {"Negative": [], "Neutral": [], "Positive": []}
    for score in score_list:
        if score <= 5:
            bins["Negative"].append(score)
        elif score <= 8:
            bins["Neutral"].append(score)
        else:
            bins["Positive"].append(score)
    return bins
print(score_counter())
"""



#########################
# Dictionaries in python.
#########################

"""
chai_types= {"Masala": "Spicy", "Salt": "Salty",
             "Ginger": "Zesty", "Green": "Mild", 
             "Kashmiri": "Not in the menu"}
print(chai_types)
print(chai_types["Masala"])


#...Methods with dictionaries in python.
chai_types["Green"]= "Fresh"    # Changing a value of a tea in python's dictionary.
print(chai_types, "\n")
print(chai_types.get("Salt"))

greentea= chai_types.get("Green")
print(greentea)

chai_types.update({"Salt": "Undrinkable"})
print(chai_types, "\n")

# We don't need .update() for one key.
chai_types["Salt"]= "Salty"
print(chai_types)


# Looping on a dictionary.
for chai in chai_types:
    print(chai)

print("\n")

for key, value in chai_types.items():
    #We can print both key and value inside the for loop.
    print(key, value)
print("\n")

if "Green" in chai_types:
    print("I have Green tea.", "\n")
"""



#############################
#..Function testing in python.
#############################
"""

import random
random.seed(42)

score_list= [1,2,3,4,5,6,7,8,9,10]
def score_counter(score_list):
    bins= {"Negative": [], "Neutral": [], "Positive": []}
    for score in score_list:
        if score <= 5:
            bins["Negative"].append(score)
        elif score <= 8:
            bins["Neutral"].append(score)
        else:
            bins["Positive"].append(score)
    Neg= len(bins["Negative"])
    Neu= len(bins["Neutral"])
    Pos= len(bins["Positive"])
    print(f"Negative: {Neg}, Neutral: {Neu}, Positive: {Pos}")

possible_scores= list(range(1,11))
score_list1 = random.choices(possible_scores, weights=[8,8,8,8,8,3,3,4,20,30], k=10)
score_list2 = random.choices(possible_scores, weights=[1,2,3,4,5,10,15,15,7,9], k=450)
score_list3 = random.choices(possible_scores, weights=[1,2,3,4,4,5,5,10,15,25], k=10000)

print('Test 1:')
score_counter(score_list1)
print('\nTest 2: ')
score_counter(score_list2)
print('\nTest 3: ')
score_counter(score_list3)


# ID validator in python.

def id_validator(verified_ids, feedback_ids):
    unverified_feedback= [id for id in feedback_ids if id not in verified_ids]

    percent_unverified= (len(unverified_feedback)/len(feedback_ids))*100
    print(len(unverified_feedback), 'of', len(feedback_ids), "ID's unverified.")
    print(str(round(percent_unverified, 2)) + "% ID's unverified.")

id_validator(['1','2','3','4','5','6','7','8'], ['1','2','9','11','3'])

import ada_c2_labs as lab

print('Test 1: ')
ver1, fb1 = lab.lists_gen(8, 20, 15, 15)

id_validator(ver1, fb1)


#################
#..Sales counter.
#################
sales = [[2.75], [50.0, 50.0], [150.46, 200.12, 111.30]]
def purchases_100(sales):
    result= []
    for sale in sales:
        if sum(sale) > 100:
            result.append(sale)
    return result
purchases_100(sales)


##################################
#..Testing Sales_counter function.
##################################
import ada_c2_labs as lab
sales1 = lab.sales_data_generator(n_customers=10, seed=1)  
print('Test 1:', purchases_100(sales1))

sales2 = lab.sales_data_generator(n_customers=150, seed=18)
print('Test 2:', purchases_100(sales2))

sales3 = lab.sales_data_generator(n_customers=1275, seed=42)
print('Test 3:', purchases_100(sales3))
"""


##################################
#..Working with strings in python.
##################################

"""
word= "python"
print(word[0]) # p
print(word[3]) # h

# String slicing
text= "Python"

print(text[0:2])
print(text[2:4])
print(text[4:6], "\n")
print(text[:1])
print(text[:2])
print(text[:3]) # Pyt. Starts slicing from the begining to letter 
print(text[:4])
print(text[:5])
print(text[:6], "\n")

#..[::n] picks index 0, n, 2n, 3n... and stops when index goes out of string length.
print(text[::3]) # Ph. start from beginning, jump every 3rd character of 'text'.
print(text[::1])  # Python → every 1st char (all).

print("\n") #...Prints an empty line.
# Printing the index of a character in a string.
print(text.index("P"))
print(text.index("y"))
print(text.index("t"))
print(text.index("h"))
print(text.index("o"))
print(text.index("n"))

# Using square brackets to perform indexing.
my_string, my_list = 'Mississippi half-step' , [1, 'unladen', 'swallow']

print( "\n", my_string[0])
print(my_list[1])
print(my_list[-1])
print(my_list[2])


# Assessing part of the string using square brackets.
print(my_list[0:2])
print(my_string[-9:]) # Assessing substring from the end.
print(my_string[:11])

### Assessing string from with steps.
#my_string[start:stop:step]
greeting= "Hello World!"
print("\n", greeting[::2])   # Every 2nd character: Hlo ol!
print(greeting[::-1])  # Reversed: !dlroW ,olleH

# format() method in strings.
name= 'Khan'
number= 3
print("Hello {}. Your lucky number is {}.".format(name, number))

# Using integers to insert into strings to indicate the order value of insertion.
print("Hello {1}. Your lucky number is {0}.\n".format(number, name))

# Setting a limit in the decimal places on the number of the output.
price= 7.75
with_tax= price*1.07
print("Base price: ${:.2f} USD \nWith tax: $ {:.2f} USD.\n".format(price, with_tax))


def to_celsius(x):
    return (x-32)* 5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
"""


# String formatting and regular expressions.
x = 'values'
y = 100

print('''String formatting lets you insert {} into strings.
They can even be numbers, like {}.'''.format(x, y))

