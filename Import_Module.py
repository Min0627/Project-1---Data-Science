#!/usr/bin/env python
# coding: utf-8

# In[32]:


# module in .py
import sys
sys.path.append("C:\\Users\\LENOVO\\Downloads\\Project 1 Data Science")
from Vehicle_System import Vehicle, Car, Motorcycle, create_vehicles

vehicles = create_vehicles()

for i, vehicle in enumerate(vehicles, 1):
    print(f"Vehicle {i}: {vehicle.display_info()}")

