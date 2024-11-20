#Program to print Alphabet Fibonacii series
n1='A'
n2='B'
num=int(input("Enter the number of elements:"))
if num>0:
    print(n1)
    print(n2)
    for i in range(2,num):
        n3=n2+n1
        print(n3)
        n1=n2
        n2=n3
else:
    print("Please Enter valid integer")