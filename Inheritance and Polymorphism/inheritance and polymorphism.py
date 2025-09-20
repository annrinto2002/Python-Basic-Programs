class Vehicles:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display_info(self):
        print(self.brand)
        print(self.model)

class Car(Vehicles):
    def __init__(self,num_doors,brand,model):
        super().__init__(brand,model)
        self.num_doors=num_doors

    def display_info(self):
        print(self.num_doors)

class Bike(Vehicles):
    def __init__(self,engine_capacity,brand,model):
        super().__init__(brand,model)
        self.engine_capacity=engine_capacity

    def display_info(self):
        print(self.engine_capacity)

class Truck(Vehicles):
    def __init__(self,load_capacity,brand,model):
        super().__init__(brand,model)
        self.load_capacity=load_capacity

    def display_info(self):
        print(self.load_capacity)
    
car1=Car(4,"Toyota","Corolla")
bike1=Bike(2000,"Honda","CBR600RR")
truck1=Truck(300,"Ford","F-150")

print(car1.display_info())
print(bike1.display_info())
print(truck1.display_info())





        





