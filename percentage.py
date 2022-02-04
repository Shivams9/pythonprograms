p = 45
c = 46
m = 40
if p<40 or c<40 or m<40:
    print("Fail")
else:
    percent = (p + c + m) / 3
    print(percent)
    if percent<50:
        print("Third")
    elif percent<60:
        print("Second")
    else:
        print("First")
