#Check Palindrome Number or String  : ye vo function hota hai jo ki reverse hota hai brabar

 # a = 'ramar'
# if ( a[0]==a[-1]):   #BAS ISME A Ko ZERO MAN K A Ko LAST SE BADAL DEYA AUR GHTA DEYA


s = input("Enter Value  ")   #enter input 
reverse = s[::-1]            # : start and  end point: otherwise it take EntireString ,slice  step use -1 to step back
if (s==reverse):             #reverse function is known as Palindrome 
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
    #Output : MadaM ,NamaN and 121 ,22322 is Palindrome
    
  # 2 nd method  
# x=int(input("Enter any Interger value: "))   #interger se string me change karne k leye bas str use kar k no se string me ho jayega
# print(str(x) == str(x)[::-1])
