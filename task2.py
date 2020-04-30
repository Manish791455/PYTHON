#['m', 'a', 'n', 'i', 's', 'h']
name = 'manish'
newname = []
for letter in name:
    newname.append(letter)
print(newname) 

# another method list comprehension ['m', 'a', 'n', 'i', 's', 'h']

third_list = [letter for letter in name]
print(third_list)


#print 100 numbers
for numb in range(1,101):
    print(numb, end=' ')


# another method list comprehension print 100 numbers
fourth_list = [numb for numb in range(1,101)]
print(fourth_list)


#list comprehension
first_list = [1,2,3,4,5,6,7,8,9]
second_list = []
for num in first_list:
    second_list.append(num)
print('second list is :', second_list) 

# another method list comprehension
second_list = [num for num in first_list]
print(second_list)



#print even numbers below 100
for num in range(1, 101):
    if num % 2 == 0:
        print(num)
    else:
        print('{} is a odd number'.format(num))

#  another method if else in list comprehension print even numbers below 100 
even_numbers = [num if num % 2 == 0 else ' {} is a odd number' .format(num) for num in range(1, 101)]
print(even_numbers)

#find square root in python
import math
print('enter your number')
number = int(input())
print(int(math.sqrt(number)))

#find square root of the list
import math
number_list = [2,4,8,16]
for num in number_list:
    print(int(math.sqrt(num)))

#another method find square root of the list
import math
square_root_list = [int(math.sqrt(num)) for num in number_list ]
print(square_root_list)

#print table
print('enter your number')
number = int(input())
for num in range(1,11):
    print('{} * {} = {}'.format(number, num, number * num))


#nested for loop
nestlist = []
for n in [1,2,3]:
    for y in [100, 200, 300]:
        nestlist.append(n * y)
print(nestlist) 
# another method for loop
first_list = [1,2,3]
second_list = [100,200,300]
for n in first_list:
    for y in second_list:
        print(n * y) 
#another method for loop
result = [n * y for n in first_list for y in second_list ]
print(result) 
             








