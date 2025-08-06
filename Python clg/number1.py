#multiplication table
n=int(input("enter number for multiplication table"))
print("multiplication table is :")
for i in range(1,11):
    print(n*i)

#palindrome
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10 

if original == reverse:
    print("Given number is a palindrome")
else:
    print("Not a palindrome")


 