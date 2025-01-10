# Python comes with an number of built-in types (lists, sets, dict, ...)
# Let's imagine we want to create a new type in python for example 2 dimensionnal points (with a x and y value)
# we can create an entire class of object to be able to represent this datastructure
# a class is a template for a type of object, example :

#after we define what a "Point" is, we will be able to create other points
class Point():
    #When I create a point : "What should happen?" __init__ is function that will imediatly be called each time we create a new point
    def __init__(self, input1, input2):
        self.x = input1
        self.x = input2

p = Point(2, 8)
print(p.x)
print(p.y)

# So what we have here is a function called init that creates a point by storing the two inputs inside of the object, 
# inside of a property called x and a property called y, such that later I can create a point which calls this init function implicitly. 
# And after we've created the point, I can access the data inside of it. I can say print out whatever p.x is equal to, print out whatever p.y is equal to as well. 