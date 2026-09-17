# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jesse Rodriguez Yulian Villarreal Amber Perez Jose Godoy
# Section: ENGR 102 M02
# Assignment: Lab 4
# Date: 09/16/26

a,b,c = [int(input(f"Please enter the coefficient {x}: ")) for x in "ABC"]
q = ""
if a == 1:
    q = "x^2"
elif a == -1:
    q = "- x^2"
elif a < -1:
    q = f"- {-a}x^2"
elif a > 1:
    q = f"{a}x^2"
if b > 0:
    if a == 0:
        if b == 1:
            q = "x"
        else:
            q = f"{b}x"
    elif b == 1:
        q += " + x"
    else:
        q += f" + {b}x"
elif b < 0:
    if a == 0:
        if b == -1:
            q = "- x"
        else:
            q = f"- {-b}x"
    elif b == -1:
        q += " - x"
    else:
        q += f" - {-b}x"
if c > 0:
    q += f" + {c}"
elif c < 0:
    q += f" - {-c}"
print(f"The quadratic equation is {q} = 0")
# howdy
