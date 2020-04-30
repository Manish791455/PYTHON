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

#find square root in python
import math
print('enter your number')
number = int(input())
print(math.sqrt(number))

#calculate the area of a traingle
print('enter values')
a = int(input())
b = int(input())
c = int(input())
#calculate semi-parameter
s = (a + b + c) / 2
print(int(s))
#calculate the area
import math
area = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(area)

