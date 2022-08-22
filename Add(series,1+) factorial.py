#Write a program to print  Factorial of a Given number...Py3..>

#n=5
n=int(input("Given number "))
i = 0   #i range hai jo ki 1 se start hoga
sum = 0   #sum ki value = 0 
while(i<=n):   #i mtlb 1 
    sum =sum+i    #sum+1 mtlb 0 + 1 =1
    i = i+1       #i mtlb 1 = (1+1)=2 wapis loop chlega jo ki While condition se start hoga i+1 tak
    
    print("Sum ",sum, end=",")         #sum ki hue sari value print karega
    
    #Output  : Given number 3 = 1, 1+2=3, 1+2+3=6
