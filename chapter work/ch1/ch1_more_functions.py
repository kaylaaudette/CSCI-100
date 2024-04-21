def hi(): # this function had no parameters
    print("Hi") # it doesn't return anything
    
def bye(name): # this function has one parameters
    print("Goodbye, ", name) # it doesn't return anything
        
def sum_version1(num1, num2): # this function has two parameters
    return num1 + num2 # it returns the sum

def sum_version2(num1, num2): # this function has two parameters
    print(num1 + num2) # it doesn't return anything

if __name__ == "__main__":
