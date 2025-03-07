class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand      # __ means private
        self.__model=model
        Car.total_car+=1
    
    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    #encapsulation
    def get_brand(self):
        return self.__brand

    #polymorphism
    def fuel_type(self):
        return "petrol or diesel"

    #static method
    @staticmethod
    def general_description():
        return "cars are mean of transport"
    
    #read only and make the function use like variable
    @property
    def model(self):
        return self.__model
    
#inheritance  
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    #polymorphism
    def fuel_type(self):
        return "electric charge"
    

my_tesla=ElectricCar("tesla","model s","85kwh")
# print(my_tesla.brand)             #if not encapsulated
# print(my_tesla.get_brand())       #if encapsulated
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())

my_car=Car("toyota","corolla")
# my_car.model="raees"              #cause it is read only

print(my_car.fuel_type())
# print(my_car.brand)
print(my_car.model)
# print(my_car.full_name())

# print(my_car.general_description())     #cause method is static
# print(Car.total_car)

# print(Car.general_description())