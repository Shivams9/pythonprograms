# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year

#year=2016=Leap Year
year=int(input())
ly=4
if year % 400==0 or year%4==0 and year%100!=0:
    print("leap")
else:
    print("not leap year")
