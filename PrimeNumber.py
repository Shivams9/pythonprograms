#Prime Number
num=int(input('Enter number :'))

if num ==1:
    print('Not a prime number')
elif num>1:
    for i in range(2,num):
        if num %i==0:
            print("it's not prime")
            break
        else:
            print('This is prime Number : ')
            break
            
