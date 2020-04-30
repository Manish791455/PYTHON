class book():
    def __init__(self,author,pages):
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'this book is written by {self.author} and total pages of this book is {self.pages}'
    def __len__(self):
        return self.pages    
    
jungle = book('jerry',230)
dream_big = book('coral',500)
print(jungle)
print(dream_big)
print(len(jungle))

