# Fibonacci number or series

num = int(input("Enter how many fibonacci numbers you want to generate:"))
a=0
b=1
sum=0
if(num<=0):
    print("Wrong input, not possible")
elif(num==1):
    print(a)
elif(num>=2):
    for i in range(0,num):
        print(sum,end=' ')
        a=b
        b=sum
        sum=a+b
   
