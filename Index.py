class Vehicle:

    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage  

class Car(Vehicle):
    def __init__(self,brand,colour,name,max_speed,milage):
        self.brand = brand
        self.colour = colour

        Vehicle.__init__(self, name, max_speed, milage)
BMW = Car("BMW","Black","BMW X7",240,18)        
print("Vehicle Name:",BMW.name,"Speed:",BMW.max_speed,"Milage:",BMW.milage,"Brand:",BMW.brand,"Colour:",BMW.colour)