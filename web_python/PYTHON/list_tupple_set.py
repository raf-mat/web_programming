#Little program for fun
age = int(input("type your age: "))

if age < 18:
    print(f"{age} is young")

else:
    print(f"{age} is old")

#List (print Harry) : a list is mutable (we can add, modify, delete a value)
    #Define a list of name
names = ["Harry", "Ron", "Hermione"]

print(names[0])
    #add value tothe list
names.append("Draco")
    #sort the list
names.sort()
print(names)

#tupple
coordinateX = 10.0
coordinateY = 20.0

coordinate = (10.0, 20,0)

#Set
    #Create an empty set
s = set()

    #Add elements to set (set is mathematical term, no elements ever appear more than once in a set)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
    #remove the element = 2
s.remove(2)
print(s)
    #print the lengh os the set (how many elements are in the set (s))
print(f"The set has {len(s)} elements.")

