#small function
def addition(a,b,c,d,e):
    print (a+b+c+d+e)
addition(2,3,4,4,6)

#small function another method
def addition(a, b, c, d, e):
    return sum((a, b, c, d, e))
print(addition(2, 3, 4, 4, 6))

#small function another method
def addition(a, b, c, d, e=6):
    return sum((a, b, c, d, e))
print(addition(2, 3, 4, 4,))

#small function with args
def addition(*args):
    return sum((args))
print(addition(2, 3, 4, 4, 6))

#small function with kwargs # kwargs returns dictionary
def food(**kwargs):
    print(kwargs)
    if 'fruits' in kwargs:
        print('thank you for offering {}'.format(kwargs['fruits']))
 
food(fruits = 'apple', veg = 'tomato', snacks = 'coffee')

#small function with args and kwargs
def fun(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f'student name is {kwargs["name"]} and roll no. is {args[0]}')
fun(2,3,4, name = 'manish', name2 = 'sandeep') 

#using args print even numbers
def evenno(*args):
    for n in args:
        if n%2 == 0:
            print(f'{n} is evevn number')

evenno(1,2,3,4,5,6,7,8,9)

#print even numbers in a newlist
def numbers(*args):
    evenno = []
    for n in args:
        if n%2 == 0:
            evenno.append(n)
            
    print(evenno)
numbers(1,2,3,4,5,6,7,8,9)

#find area of square for each side
list_of_sides = [1,2,3,4,5,6]
for sides in list_of_sides:
    print(sides**2)

#find area of square for each side by function
def square(*args):
    for s in args:
        print(s**2)

square(2,3,4,5,6)

#small function using map
def addition(n):
    return n + n

numbers = [1,2,3,4] 
result = map(addition,numbers)
print(list(result))
# double all numbers using map and lambda
numbers = [1,2,3,4]
result = map(lambda x : x + x, numbers)
print(list(result))
#add two lists using map and lambda   
n = [1,2,3]
m = [2,3,4]
result = map(lambda n,m: n + m, n, m)
print(list(result))
#list of strings
names = ['cat', 'bat', 'rat']
result = map(list,names)
print(list(result))