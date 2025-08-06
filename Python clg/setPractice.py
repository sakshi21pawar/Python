#sets in python
s={10,20,40}
print(s)
print(type(s))
s1={"hello",20,90,80,80}
print("s1 :",s1)

#adding element to list
s.add("bye")
print(s)

#union of sets
people = {"sakshi", "ajinkya", "siddhi"}
vampires = {"karan", "arjun"}
population = people.union(vampires)
print(population)

#intersection of sets
set1 = set([1, 2, 3, 3])  # or simply: set1 = {1, 2, 3}
set2 = set([1, 2, 3,5,6])     # or: set2 = {1, 2, 3}


    
set3 = set1.intersection(set2)

print("intersection using intersection function")
print(set3)

    
    
    