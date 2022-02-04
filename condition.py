#  condition=row+col>=n+1
# condition=row<=col
#condition = row ==col or row+col==n+1
#condition=row==col
#condition=row>=col
#condition=row,col
#row==mid or col-row==mid-1 or row+col==n+mid
#condition = row+col>=mid+1  and row+col<=n+mid and  col-row<=mid-1 and row<=mid  //[piramid]\\

n=7
mid=(n+1)//2
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row+col>=mid+1  and row+col<=n+mid and  col-row<=mid-1 and row<=mid
        if condition :
            print("0",end="")
        else:
            print(" ",end="")
    print()
