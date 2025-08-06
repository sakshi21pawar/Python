#creating a list
a=[10,20,"hello",40,True]
print(a)

#Accessing element of list
print(a[2])
print(a[4])

#type checking
print(type(a[4]))
print(type(a[1]))

b=[2]*5
print(b)

a.remove(20)
print("after remove(20)",a)
s=["apple","mongo","banana"]
#iteration over list
for item in s:
    print(item)
#append at list
s.append("chiku")
print(s)
c=s.copy()
print(c)
c.clear() #remove all elements from the list 
print("list after using clear function",c)
   #extend element
a.extend([False,5])
print(" list a after extend",a)

user_input=input("enter elements for list:")
my_list = user_input.split()
print(my_list)