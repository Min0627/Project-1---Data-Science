#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors, fuel_type):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Doors: {self.num_doors}, Fuel Type: {self.fuel_type}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine, sidecar):
        super().__init__(brand, model, year)
        self.engine = engine
        self.sidecar = sidecar

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Engine: {self.engine}cc, Sidecar: {self.sidecar}"

def create_vehicles():
    vehicles = [Vehicle("Proton", "X50", "2020"), Car("Honda", "Civic", 2021, 4, "Petrol"), 
                Motorcycle("Yamaha", "YZF-R1", 2024, 998, False),
                Car("Tesla", "Model S", 2023, 4, "Electric"),
                Motorcycle("Harley-Davidson", "Sportster", 2022, 1200, False)]
    
    return vehicles


# In[ ]:




