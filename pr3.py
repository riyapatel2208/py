def num(n):
    if n>0:
        num(n-1)
        print(n,end=" ")
n=int(input("Eenter the number:"))
num(n)