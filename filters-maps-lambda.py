def func(n):
    return n*n
print(func(5))
#finding square
def square(a):
    return a*a
square_list = [1,2,3,4,4]
result = map(square,square_list)
print(list(result))
#another method using map
def square(a):
    return a*a
square_list = [1,2,3,4,4]
print(list(map(square,square_list)))
#using for loop it prints each item
def square(a):
    return a*a
square_list = [1,2,3,4,4]
for item in map(square,square_list):
    print(item)
#filters are using for filters
def even_no(num):
    return num % 2 == 0
square_list = [2,3,4,5,6,7,8]    
for item in filter(even_no,square_list):
     print(item)
#filters in list
print(list(filter(even_no,square_list)))     
#if we use map it give true,false        
for item in map(even_no,square_list):
     print(item)     
#SMALLFUNC NO LAMBDA
def func(n):
    return n*n
print(func(5))
#WITH LAMBDA
func = lambda n: n * n      
print(func(5))
#area of a traingle
def traingle(a,b):
    return a*b
print(traingle(2,3))
#area of a traingle wth lambda
traingle = lambda a,b : a*b
print(traingle(2,3))
#using map and lambda not applied
def square(f):
    return f*f
square_list = [1,2,3,4,5]
for item in map(square,square_list):
    print(item)
#applied mpas and lambda
print(list(map(lambda f:f*f,square_list)))
###
def even_no(num):
    return num % 2 == 0
square_list = [2,3,4,5,6,7,8]    
for item in filter(even_no,square_list):
     print(item)
print(list(filter(even_no,square_list)))     
##using filters and lambda
print(list(filter(lambda d% 2 == 0,square_list)))      