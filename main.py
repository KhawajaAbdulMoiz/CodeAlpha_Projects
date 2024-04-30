# Create a Fibonacci Generator in python
 
print("==========FIBONACCI GENERATOR==========")
num=int(input("Enter the number for the Fabonacci Series : "))

n1=0
n2=1
sum=0
if(num<0):
    print("Enter number which is greator than 0")
if(num==0):
    print(n1)    
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2

    