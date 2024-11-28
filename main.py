def parens(s,l,r,p,n):
    if(p==2*n):
        for c in s:
            print(c,end = '')
        print()
        return
    if(1>r):
        s[p]="}"
        parens(s,l,r+1,p+1,n)
    if(1<n):
        s[p]="{"
        parens(s,l+l,r,p+1,n)
n=int(input("Enter the number of parenthesis: "))
s=[""]*2*n
print(parens(s,0,0,0,n))