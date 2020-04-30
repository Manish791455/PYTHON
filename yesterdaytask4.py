# 1) python program finding square root
#to find square root in python we import math
print('enter your number')
n = int(input())
import math
print(math.sqrt(n))

#..............................
# 2) python program swap two numbers
#swap means we are chaging values with variables
a = 5
b = 6
#before swap
print(a)
print(b)
#swapping take a new variable and swap with a
new = a
#swap a with b
a = b
#swap b with new variable
b = new
#after swap
print('The value of a is:', a)
print('The value of b is :', b)
#................................

#@ @ @ @ @ @ @ @
# 3) python programm to generate a random munber
# we generate random numbers using import random

import random
# randint means -it takes integers(start,end) and give random number
#inclusive range
print(random.randint(1,20))

import random
#let generate -values (here int -5-4-3-2-1 0 12345, so we write in this way)
print(random.randint(-20,-1))

import random
#here it will not print 500 but it prints between tange of 1000 to 4999
#exclusive range
print(random.randrange(1000,5000))

import random
#here 4 is multiply with range of 2 t0 199 and give random no.
print(random.randrange(2,200,4))

#if i need a random number with only one value we use secrets
#rand below means it give random value of below 20
import secrets
print(secrets.randbelow(20))

#using for lopp print random no. 
list = [1,20]
for i in range(1,20):
    result = (random.randint(1,20))
print(result)    
#@ @ @ @ @ @ @ @

# 4)to convert kilometers to miles
# 1 KILOMETER = O.621371 MILES
kilometers = 25.5
k_m = 0.621371
mile = kilometers * k_m
print('{} kilometers is equal to {} miles'.format(kilometers, mile))

# 1 kg = 1000 grams so we need 100 kg in grams
kg = 100
kg_gm = 1000
grams = kg * kg_gm
print('{} kg is equal to {} grams'.format(kg, grams))

# 5) check leap years
print(' please enter year')
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')      
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


# 6) python program to display multiplication number
print('enter your number')
number = int(input())
for i in range(1,11):
    print(f'{number} x {i} =', number*i)

# 7) find sum of natural numbers
n = int(input())
s = n*(n+1)/2
print(s)

# 8) python program to make A SIMPLE PROGRAM
def addition(a,b):
    print('sum is :', a+b)
def subtraction(a,b):
    print('subtraction is :', a-b)
def multiplication(a,b):
    print('multiplication is :', a*b)
def division(a,b):
    print('division is :', a/b)
def reminder(a,b):
    print('reminder is :', a%b) 
print('welcome to calculator')
print('enter first number')
n1 = int(input())
print('enter second number')
n2 = int(input())
addition(n1,n2)
subtraction(n1,n2)
multiplication(n1,n2)
division(n1,n2)
reminder(n1,n2)

# 9) finding area of a traingle
a = int(input())
b = int(input())
c = int(input())
s = (a + b + c)/2
print(s)
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('the area of a traingle is',area)

