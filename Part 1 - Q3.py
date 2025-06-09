#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Input
students = int(input("Enter number of students: "))
grades = []
for i in range(students):
    grade = float(input(f"Enter grade for student {i+1}: "))
    grades.append(grade)

# Processing
average = sum(grades) / students
highest = max(grades)
lowest = min(grades)

# Output
print(f"\nClass Average: {average:.2f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")


# In[ ]:




