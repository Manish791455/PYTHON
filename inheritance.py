# 1)
class Animal(): # THIS IA BASE CLASS
    def __init__(self):
        pass
    def about(self):
        print('this animal belongs to mamal')
    def func(self):
        print('this dog barks normally')        
harry = Animal()
harry.about()
harry.func()  

# 2) inheritance 
class dog2(Animal): # about this class and method # both animals are mamals , but barking are differnt.
    def __init__(self):
        pass
    def func(self):
        print('this dog barks loudly')
poter = dog2()
poter.about()
poter.func()

# 3)
class dog3(dog2): # about this class and method # both animals are mamals , but barking are differnt.
    def __init__(self):
        pass
    def func(self):
        print('this dog barks loudly')
poter = dog3()
poter.about()
poter.func()

# 4)
from i2 import newdog
class dog4(newdog):
    def __init__(self):
        pass
    
max = dog4()
max.hyb()
max.dang()        


