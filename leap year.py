year=2016
ly=4
if year % 400==0 or year%4==0 and year%100!=0:
    print("leap")
else:
    print("not leap year")
