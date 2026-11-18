import numpy as np
data = np.loadtxt("module12quizF26.txt", dtype = int).reshape(100,100)
a = data[73, :5].mean()
b = data[7,:5].min()
c = data[60, -5:].max()
d = data[:3, 18].sum()
e = data[-3:, 51].min()

shift = int(a-b+c-d+e)
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = ""
for letter in "uzijaktocji":
    message += alphabet[(alphabet.index(letter) + shift) % 26]

print("Message:", message)
print("Shift:", shift)