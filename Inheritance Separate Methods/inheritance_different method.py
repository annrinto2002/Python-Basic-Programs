class Vehicles:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def ShowDetails(self):
        print(self.brand)
        print(self.model)

class Car(Vehicles):
    def __init__(self,num_doors,fuel_type,brand,model):
        super().__init__(brand,model)
        self.num_doors=num_doors
        self.fuel_type=fuel_type

    def CarDetails(self):
        print(self.num_doors)
        print(self.fuel_type)

class Bike(Vehicles):
    def __init__(self,engine_capacity,brand,model):
        super().__init__(brand,model)
        self.engine_capacity=engine_capacity

    def BikeDetails(self):
        print(self.engine_capacity)

class Truck(Vehicles):
    def __init__(self,load_capacity,brand,model):
        super().__init__(brand,model)
        self.load_capacity=load_capacity

    def TruckDetails(self):
        print(self.load_capacity)

car1=Car(4,"Petrol","Toyota","Corolla")
bike1=Bike(2000,"Honda","CBR600RR")
truck1=Truck(300,"Ford","F-150")

car1.CarDetails()
bike1.BikeDetails()
truck1.TruckDetails()




        





