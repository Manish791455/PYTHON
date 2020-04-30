class mobiles():
    def __init__(self):
        print('welcome to mobile world')
    def display(self):
        print('It is with full hd display')
    def battery(self):
        print('power master with 5000 mah battery')
    def processor(self):
        print('snapdragon 665 ')
    def ram(self):
        print('4gb ram')
    def coast(self):
        print('10000')
next_level = mobiles()
next_level.display()
next_level.battery()
next_level.processor()
next_level.ram()
next_level.coast()

class mobile2(mobiles):
    def __init__(self):
        print('welcome to mobile world')
    def processor(self):
        print('snapdragon 720GA pricessor')
    def ram(self):
        print('6gb ram')
    def coast(self):
        print('18000')    

next_level2 = mobile2()
next_level2.display()
next_level2.battery()
next_level2.processor()
next_level2.ram()
next_level2.coast()         
