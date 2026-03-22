def simpleIntrest(p=1000, t=5, r= 10):
    result = p*t*r/100
    print("Simple Intrest: ",result)
    
simpleIntrest()


# Palindrom

def palindrom(string):
    reverse = string[::-1]
    if(string == reverse):
        print("Palindrom")
    else:
        print("Not palindrom")
        
palindrom("lol")