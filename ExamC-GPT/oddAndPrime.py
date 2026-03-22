
# Prime Number not 2 include for this (and n%2!=0)
for n in range(2, 21):
    count = 0
    for i in range(1,n+1):
        if n%i == 0 and n%2!=0:
            count = count + 1
    if count == 2:
        print(i)



# Sum of digits

n = 2; 
sumofAll = 0
for i in range(1, n+1):
    sumofAll+=i   


print(sumofAll)

