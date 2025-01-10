# define a class called Flight with one argument : capacity
class Flight():
    def __init__(self, capacity):
        #we store the value into a variable called capacity
        self.capacity = capacity
        #create a list of empty passenger
        self.passenger = []
    # let's define a new method or function to add a new passenger, Because this is a method that's going to work on an individual object, 
    # we need some way of referencing that object itself. So we'll use the keyword "self" again. 

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


#create a flight with a capacity of three with a list of empty passenger
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    succes = flight.add_passenger(person)
    if succes:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")