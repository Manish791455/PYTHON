a = 2
b = 0
try:
    print(a/b)
    
except:
    print('zero division error')

#### how we work with try and except

def log():
    while(True):
        try:
            no = int(input())
        except:
            print('we take no only')
        else:
            print('thankyou for enterimg a no atleast')
            break
log()        
