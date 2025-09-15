class Vehicle():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def ShowDetails(self):
        print(f"Brand:{self.brand},Model:{self.model}")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass
    
car=Car("Toyota"," Corolla")
bike=Bike("Honda"," CBR600RR")
truck=Truck("Ford"," F-150")

car.ShowDetails()
bike.ShowDetails()
truck.ShowDetails()

    


    
