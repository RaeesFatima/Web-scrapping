# Car Class OOP Implementation in Python

## Overview
This project demonstrates Object-Oriented Programming (OOP) principles in Python using a `Car` class and its derived classes. It includes concepts like **encapsulation, inheritance, polymorphism, static methods, properties, and multiple inheritance**.

## Features Implemented
### 1. **Encapsulation**
- The `brand` and `model` attributes are private (prefixed with `__`), ensuring data protection.
- Getter method (`get_brand()`) allows controlled access to private attributes.

### 2. **Polymorphism**
- The `fuel_type()` method is overridden in the `ElectricCar` class to return "electric charge" instead of "petrol or diesel".

### 3. **Inheritance**
- The `ElectricCar` class inherits from `Car`, adding a `battery_size` attribute.
- The `ElectricCarTwo` class demonstrates multiple inheritance by inheriting from `Car`, `Battery`, and `Engine`.

### 4. **Static Methods**
- `general_description()` is a static method providing general information about cars and is accessible via the class name (`Car.general_description()`).

### 5. **Property Decorator**
- The `model` attribute is read-only, allowing access but preventing modification (`@property`).

### 6. **Class Attribute**
- `total_car` keeps track of the number of `Car` instances created.

## Classes and Methods
### **Car Class**
```python
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand  # Encapsulation
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):  # Encapsulation
        return self.__brand
    
    def fuel_type(self):  # Polymorphism
        return "petrol or diesel"
    
    @staticmethod
    def general_description():  # Static Method
        return "Cars are a means of transport"
    
    @property
    def model(self):  # Read-only property
        return self.__model
```

### **ElectricCar Class (Inheritance & Polymorphism)**
```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):  # Method Overriding (Polymorphism)
        return "electric charge"
```

### **Multiple Inheritance**
```python
class Battery:
    pass

class Engine:
    pass

class ElectricCarTwo(Car, Battery, Engine):
    pass
```

## Usage Example
```python
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.get_brand())      # Tesla
print(my_tesla.model)            # Model S (Read-only property)
print(my_tesla.battery_size)     # 85kWh
print(my_tesla.fuel_type())      # electric charge

my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())        # petrol or diesel
print(my_car.model)              # Corolla

print(Car.general_description()) # Static method call
print(Car.total_car)             # Number of car instances created
```

## Conclusion
This project demonstrates key OOP principles in Python, providing a solid foundation for building structured, maintainable, and scalable applications.

