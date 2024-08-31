#!/usr/bin/env python
# coding: utf-8

# #### Assignment 1

# - Following the materials and instructions provided in this week’s reading regarding OOP, write code demonstrating OOP in Python. Demonstrate inheritance, polymorphism, and encapsulation within the code. Submit your code to the assignment area.

# ##### Base Class

# In[1]:


# Base class
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand  # Encapsulation: Using underscore to indicate protected variable
        self._model = model

    def get_details(self):
a        return f"Brand: {self._brand}, Model: {self._model}"

    def move(self):
        return "This vehicle is moving."


# ##### Inheritance

# In[2]:


# Inheritance: Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        super().__init__(brand, model)  # Calling constructor of the base class
        self._car_type = car_type  # Encapsulation

    def get_details(self):
        return f"{super().get_details()}, Type: {self._car_type}"

    def move(self):
        return "This car is moving fast."


# Inheritance: Truck inherits from Vehicle
class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self._capacity = capacity  # Encapsulation

    def get_details(self):
        return f"{super().get_details()}, Capacity: {self._capacity} tons"

    def move(self):
        return "This truck is moving slowly with heavy load."


# ##### Polymorphism

# In[3]:


# Polymorphism: Using the same interface (move) with different implementations in derived classes
def demonstrate_vehicle_movement(vehicle):
    print(vehicle.move())


# In[4]:


# Creating instances
car = Car("Toyota", "Corolla", "Sedan")
truck = Truck("Ford", "F-150", "10")


# In[5]:


# Demonstrating encapsulation and inheritance
print(car.get_details())
print(truck.get_details())


# In[6]:


# Demonstrating polymorphism
demonstrate_vehicle_movement(car)
demonstrate_vehicle_movement(truck)


# In[ ]:




