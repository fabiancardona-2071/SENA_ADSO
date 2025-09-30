class Vehicle:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model= model
        self.price=price
        self.is_available=True
    def sell(self):
        if self.is_available:
            self.is_available= False
            print(f"el vehiculo {self.brand}. Ha sido bendido")
        else:
            print(f"el vehiculo {self.brand}. no esta disponible")
    #abstraccion
    def check_available(self):
        return self.is_available
    def get_price(self):
        return self.price
    def start_engine(self):
        raise NotImplementedError("este modo debe ser implementado por la subclase")
    def stop_engine(self):
        raise NotImplementedError("Este modo de ser implementado por la subclase")
#herencia
class Car(Vehicle):
    #polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
    #polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"el motor del coche {self.brand} se ha detenido"
        else:
            return f"el coche {self.brand} no esta disponible"
class Bike (Vehicle):
    #polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"La biscicleta {self.brand} esta en marcha"
        else:
            return f"la bicicleta {self.brand} no esta disponible"
    #poliformismo
    def start_engine(self):
        if not self.is_available:
            return f"la bicicleta {self.brand} se ha detenido"
        else: 
            return f"La bicicleta {self.brand} no esta disponible "
#herencia
class Truck(Vehicle):
    #poliformismo
    def start_engine(self):
        if not self.is_available:
            return f"el motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"
    #polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"el motor del camion {self.brand} se ha detenido"
        else:
            return f"El camion {self.brand} no esta disponible"
class customer:
    def __init__(self,name):
        self.name=name
        self.purchased_vehicles=[]
    def buy_vehicle(self,vehicle:Vehicle):
        if vehicle.check_available():
            vehicle.sell
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta disponible")
    def inquire_vehicle(self,vehicle: Vehicle):
        if vehicle.check_available():
            availablity="disponible"
        else:
            availablity="no disponible"
        print(f"El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price}")
class Dealership:
    def __init__(self):
        self.inventory=[]
        self.customers=[]
    def add_vehicles(self,vehicle: Vehicle)
        self.inventory.append(vehicle)
        print(f"el {vehicle.brand} ha sido añadido al inventario")
    def register_customer(self,customer:customer):
        self.customers.append(customer)
        print(f"el cliente {customer.name} ha sido añadido")
    def show_available_vehicle(self):
        print("vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")
car1=Car("toyota","corolla",20000)
bike1=Bike("yamaha","MT-07",7000)
truck1=Truck("volvo")