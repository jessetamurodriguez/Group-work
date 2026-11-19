# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         JOSE GODOY
# Section:      M02
# Assignment:   individual topic 12
# Date:         11/09/2026
import numpy as np
import matplotlib.pyplot as plt
x,y = 0,1
a,b,c,d = 1.02,.095,-.095,1.02
# each bracket represents a column and the first number in it is the top followed by the next being below it
Matrix = np.array([[a,c],[b,d]])
vector = np.array([x,y])
plt.title("Spiral")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(vector[0],vector[1],"bo")
for i in range (250):
    product = vector@Matrix
    vector = product
    plt.plot(vector[0],vector[1],"bo")
plt.show()