def gread(num):
    if(num >= 60):
        print("First Division")
    elif(num >= 50 ):
        print("Secound Division")
    elif(num >= 25):
        print("Third Division")
    elif(num <= 25):
        print("Failed")


a = int(input("Enter Number: "))

gread(a)