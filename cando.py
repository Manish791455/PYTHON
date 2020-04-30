a = 10
print(a)

# class in python and syntex is class class_name:
class myclass:
    a = 10 #class object 
print(myclass.a)

#object in python and syntex is  object = class_name()
class myclass:
    a = 10 #class object  
    def func(self):
        print('hello')
wish = myclass()
wish.func()
print(myclass.a)

#construction in python __init__(), We normally use it to initialize all the variables.
class mobiles:
    def __init__(self, model, color, coast):
        self.model = model
        self.coast = coast
        self.color = color 
        
redmi = mobiles(model = 'mi7', color = 'red', coast = '10000')
print(redmi.model)
print(redmi.color)
print(redmi.coast)
realme = mobiles(model = 'realme6',color = 'blue', coast = '14000')
print(realme.model)
print(realme.color)
print(realme.coast)

#object and function and follow line no 10 t0 15 easily understand
class mobile:
    def __init__(self,model, color, coast):
        self.model = model
        self.color = color
        self.coast = coast
    def details(self):
        print('Here we introduce new mobile :', self.model)
        print('dynamic color :', self.color)
        print('with low coast :', self.coast)
new_mobile = mobile('redmi 7', 'black', 10000)
new_mobile.details()

#another example foloow the above code you will get
class facebook:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def log(self):
        if self.username == 'manish' and self.password == 791455:
            print('welcome back to facebook')    
        else:
            print('log in again')
details = facebook('manish',791455)
details.log() 

#let facebook in be a input form
class facebook:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def log(self):
        if self.username == 'manish' and self.password == '791455':
            print('welcome back to facebook')    
        else:
            print('log in again')
details = facebook(input(),input())
details.log() 