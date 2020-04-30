class book():
    def __init__(self):
        print('this book belong to manish')
    def fun(self):
        print('hi')    
motivate = book()
motivate.fun()   
######
class book():
    def __init__(self,author,pages):
        self.author = author
        self.page = pages
    def __str__(self):
        return f'this book is written by {self.author} and total pages of this book is {self.page}'
    def __len__(self):
        return self.page 
    def __del__(self):
        print('deleted')
               
    
   
        

mybook = book('jhony',100)
book2 = book('master',200)
print(mybook)
print(book2)
print(book2)
print(len(book2))

#######


