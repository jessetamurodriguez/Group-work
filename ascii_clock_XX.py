# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jose Godoy
# Jesse Rodriguez
# Yulian Villareal
# Amber Perez
# Section: M02
# Assignment: Lab 4 group
# Date: 09/16/2026
###################################JG######################################
Font= {
":":["   ", " : ", "   ", " : ", "   "],
'0':["rrr", "r r", "r r", "r r", "rrr"],
'1':[" r ", "rr ", " r ", " r ", "rrr"],
'2':["rrr", "  r", "rrr", "r  ", "rrr"],
'3':["rrr", "  r", "rrr", "  r", "rrr"],
'4':["r r", "r r", "rrr", "  r", "  r"],
'5':["rrr", "r  ", "rrr", "  r", "rrr"],
'6':["rrr", "r  ", "rrr", "r r", "rrr"],
'7':["rrr", "  r", "  r", "  r", "  r"],
'8':["rrr", "r r", "rrr", "r r", "rrr"],
'9':["rrr", "r r", "rrr", "  r", "rrr"],
'A':[" A ", "A A", "AAA", "A A", "A A"],
'P':["PPP", "P P", "PPP", "P  ", "P  "],
'M':["M   M", "MM MM", "M M M", "M   M", "M   M"]}
permitted=["a","b","c","d","e","g","h","k","m","n","o","p","q","r","s","u","v","w","x","y","z","@","$","&","*","="]
####################YV#########################3
tm = input("Enter the time: ")
ct= input ("Choose the clock type (12 or 24): ")
pc= input("Choose your preferred character: ")
while pc not in permitted:
    pc = input("Character not permitted! Try again: ")
########################AP###########################
hours= int(tm[0:2])
minutes= tm[3:5]
if ct== "12":
    if hours==0:
        hours=12
    elif hours>12:
        hours=hours-12
        end="PM"
    else:
        end="AM"
#####################JR######################
hours=str(hours)
minutes=str(minutes)
if ct=="12":
    tm=(hours+":"+minutes+end)
if ct=="24":
    tm=(hours+":"+minutes)
for r in range(5):
    fi = ""
    for i in tm:
        if i in Font:
            grid = Font[i][r]
            grid= grid.replace("r", pc)
            fi += grid + " "
    print(fi)
