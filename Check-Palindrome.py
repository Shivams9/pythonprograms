#Write a program to Check if a string is palindrome or Not
my_str = input("Enter a string")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) ==list(rev_str):
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
    
    #Ex: MAM, is Palindorme & Shivam, is Not 
