c=55
b=34
print(c,b)
a=c-b
while a>0:
    print(a,end=" ")
    c=b
    b=a
    a=c-b
print(a)
