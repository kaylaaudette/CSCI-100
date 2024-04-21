# if true
if True:
    print("This prints if expression evaluates to True")
else:
    print("This prints if expression evaluates to False")
    
# if false
if False:
    print("This prints if expression evaluates to True")
else:
    print("This prints if expression evaluates to False")
    
x = 2
y = 5

if x==2 or y==6:
    print("x is 2")
    print("more code")
elif x==2:
    print("x is 2 again")
elif x==4:
    print("x is 4")
#else:
    #print("x is not 2")
    #print("even more code")

x=2
y=6
if x!=2:
    print("A")
    if y==5:
        print("A1")
    else:
        print("A2")
elif y==5:
    print("B")
    if (x>5):
        print("B1")
    else:
        print("B2")
else:
        print("C")
        


n = 10
k = 20
if ( (n<20) or (k==20)):# either one of them needs to be true for entire staemnt to be true
    print("True")
else:
    print("False")
    
num = 0
(num >=0) and (num < 100)

x=10
y=0
if x>5:
   print("A")
elif y<10:
    print("B")
elif x==10:
    print("C")
else:
    print("D")
    
import random
print( random.random() )

def orangeCost(lbs):
    oranges = 0.32
    shipping = 7.50
    if lbs < 100:
        cost = (oranges * lbs) + shipping 
    elif lbs > 100:
        cost = (oranges * lbs) + (shipping - 1.50)
    return(cost)


  
