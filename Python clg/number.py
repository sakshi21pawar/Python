a=int(input("enter any number"))
#printing natural number
for i in range (1,a):
    print(i , end=" ")

#sum of n natural number
sum=0
for i in range(1 ,a+1):
    sum+=i

print("\nsum of a natural number is :",sum)

#factorial 
fact=1
i=1
while i<=a:
    fact*=i
    i+=1

print("factorial of",a,"is :",fact)