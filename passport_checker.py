# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yulian Villarreal
#        Jesse Rodriguez
#        Amber Perez
#        Jose Godoy
# Section: M02
# Assignment: Lab Topic 11 (team)
# Date: 4/11/2026
REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "cid"]


filename = input("Enter the name of the file: ")


# ---------- Read the file and group lines into passports ----------
passports = []   # each passport is a list of its original lines
current = []


with open(filename, "r") as infile:
   for line in infile:
       line = line.rstrip("\n")
       if line.strip() == "":
           # Blank line = end of the current passport
           if len(current) > 0:
               passports.append(current)
               current = []
       else:
           current.append(line)


# The last passport may not be followed by a blank line
if len(current) > 0:
   passports.append(current)


# ---------- Check each passport ----------
valid_passports = []


for passport in passports:
   fields = []
   for line in passport:
       for pair in line.split():          # pairs are separated by spaces
           key = pair.split(":")[0]       # "byr:1937" -> "byr"
           fields.append(key)


   is_valid = True
   for field in REQUIRED_FIELDS:
       if field not in fields:
           is_valid = False


   if is_valid:
       valid_passports.append(passport)


# ---------- Write the valid passports, one blank line between each ----------
with open("valid_passports.txt", "w") as outfile:
   for index in range(len(valid_passports)):
       if index > 0:
           outfile.write("\n")
       for line in valid_passports[index]:
           outfile.write(line + "\n")


print(f"There are {len(valid_passports)} valid passports")
