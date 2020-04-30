class account:
    def __init__(self,username = 'manish',balance = 100):
        self.username = username
        self.balance = balance
        print(f'Hey {username} Hey your account balance is {self.balance}, please ad an ammount')
    def deposit(self,amount):
        self.balance += amount
        print(f'Hey {self.username} your amount is successfilly deposited total balance:  {self.balance}')
        print('you can withdrawl your cash at any time')
    def withdraw(self,amount):
        if self.balance == 0:
            print('in sufficient balance')

        else:
            
            self.balance -= amount
            print(f'your amount is successfully credited remaining balance: {self.balance}')
            
     #again withdraw cash       
    def awithdraw(self,amount):
        if self.balance == 0:
            print('in sufficient balance')
        else:    
            self.balance -= amount
            print(f'your amount is successfully credited remaining balance: {self.balance}')            
d = account()
d.deposit(int(input()))
d.withdraw(int(input()))
d.awithdraw(int(input()))

        

        