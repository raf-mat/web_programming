#Ask user for their name and  Remove whitespace from str and capitalize user's name
name = input("what's your name? ").strip().title()


#Split user's name into first name and last name
first, last = name.split(" ")

#Say Hello To user  ' 3 possibilities (1st best practice)
print (f"hello, {first}")
print ("hello,",name)
print ("hello, " + name)
