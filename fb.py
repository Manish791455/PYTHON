class facebook():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def post(self,newpost):
        print(f' hey {self.username}your post has been updated as {newpost} ')
manish = facebook('manish',791455)
manish.post(input())            


         