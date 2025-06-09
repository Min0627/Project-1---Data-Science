#!/usr/bin/env python
# coding: utf-8

# In[114]:


import numpy as np

np.random.seed(42)

#Two Arrays of each size
A = np.random.rand(5,)
B = np.random.rand(5,)
C = np.random.rand(3,3)
D = np.random.rand(3,3)
E = np.random.rand(2,4)
F = np.random.rand(2,4)
G = np.random.rand(4,2)
H = np.random.rand(4,2)
I = np.random.rand(5,5)
J = np.random.rand(5,5)


# Display all arrays
print("-"*40)
print("All Arrays from A to J".center(40))
print("-"*40)
print("Array A (1D):\n", A)
print("\nArray B (1D):\n", B)
print("\nArray C (3x3):\n", C)
print("\nArray D (3x3):\n", D)
print("\nArray E (2x4):\n", E)
print("\nArray F (2x4):\n", F)
print("\nArray G (4x2):\n", G)
print("\nArray H (4x2):\n", H)
print("\nArray I (5x5):\n", I)
print("\nArray J (5x5):\n", J)


#Single Array
print("\n" + "-"*40)
print("1. Single array operations:")
print("-"*40)

sqrt_A = np.sqrt(A)
print("\n1.1 ~ Square Root of A:\n", sqrt_A)

exp_A = np.exp(A)
print("\n1.2 ~ Exponential of A:\n", exp_A)

abs_B = np.abs(B)
print("\n1.3 ~ Absolute Value of B:\n", abs_B)

log_B = np.log(B)
print("\n1.4 ~ Logarithm of B:\n", log_B)

std_C = np.std(C)
print("\n1.5 ~ Standard deviation of C:\n", min_C)

cos_D = np.cos(D)
print("\n1.6 ~ Cosine of D:\n", cos_D)

sum_E = np.sum(E)
print("\n1.7 ~ Sum of E:\n", sum_E)

mean_F = np.mean(F)
print("\n1.8 ~ Mean of F:\n", mean_F)

round_G = np.round(G)
print("\n1.9 ~ Round of G:\n", round_G)

transpose_H = np.transpose(H)
print("\n1.10 ~ Transpose of H:\n", transpose_H)


#Two Array same size AB, CD, EF, GH, IJ
print("\n\n" + "-"*60)
print("2. Two arrays of the same size operations:")
print("-"*60)

add_CD = np.add(C, D)
print("\n2.1 ~ C + D:\n", add_CD)

multy_GH = np.multiply(G, H)
print("\n2.2 ~ G * H:\n", multy_GH)

sub_IJ = np.subtract(I, J)
print("\n2.3 ~ I - J:\n", sub_IJ)

div_EF = np.divide(E, F)
print("\n2.4 ~ E / F:\n", div_EF)

great_AB = np.greater(A, B)
print("\n2.5 ~ A > B:\n", great_AB)

mod_EF = np.mod(E, F)
print("\n2.6 ~ E % F:\n", mod_EF)

logic_and_AB = np.logical_and(A > 0.5, B < 0.5)
print("\n2.7 ~ A > 0.5 AND B < 0.5:\n", logic_and_AB)

logic_or_IJ = np.logical_or(I > 0.5, J < 0.5)
print("\n2.8 ~ I > 0.5 OR J < 0.5:\n", logic_or_IJ)

power_GH = np.power(G, H)
print("\n2.9 ~ G Power of H:\n", power_GH)

max_CD = np.maximum(C, D)
print("\n2.10 ~ Maximum of C and D:\n", max_CD)

min_EF = np.minimum(E, F)
print("\n2.11 ~ Minimum of E and F:\n", min_EF)

#Two Arrays Diff Size
print("\n\n" + "-"*60)
print("3. Two arrays of different size operations:")
print("-"*60)

dot_FG = np.dot(F, G)
print("\n3.1 ~ Dot product of F and G:\n", dot_FG)

trace_dot_FG = np.trace(dot_FG)
print("\n3.2 ~ Trace of Dot product of F and G:", trace_dot_FG)

det_dot_FG = np.linalg.det(dot_FG)  
print("\n3.3 ~ Determinant of Dot product of F and G:", det_dot_FG)

inv_dot_FG = np.linalg.inv(dot_FG) 
print("\n3.4 ~ Inverse of Dot product of F and G:\n", inv_dot_FG)


# In[ ]:





# In[ ]:





# In[ ]:




