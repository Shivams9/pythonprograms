#Check Palindrome Number or String  :


s = input("Enter Value  ")   #enter input 
reverse = s[::-1]            # : start and  end point: otherwise it take EntireString ,slice  step use -1 to step back
if (s==reverse):             #reverse function is known as Palindrome 
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
    #Output : MadaM ,NamaN and 121 ,22322 is Palindrome
