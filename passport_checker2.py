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
# pid (passport ID) is not required, so it is not in this list
REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "cid"]
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
HEX_CHARS = "0123456789abcdef"




def year_ok(text, low, high):
   """Four digits, between low and high inclusive."""
   if len(text) != 4 or not text.isdigit():
       return False
   return low <= int(text) <= high




def height_ok(text):
   """A number followed by cm (150-193) or in (59-76)."""
   number = text[:-2]
   unit = text[-2:]
   if not number.isdigit():
       return False
   if unit == "cm":
       return 150 <= int(number) <= 193
   if unit == "in":
       return 59 <= int(number) <= 76
   return False




def hair_ok(text):
   """A # followed by exactly 6 characters from 0-9 or a-f."""
   if len(text) != 7 or text[0] != "#":
       return False
   for char in text[1:]:
       if char not in HEX_CHARS:
           return False
   return True




def country_ok(text):
   """A three-digit number with no leading zero (100-999)."""
   return len(text) == 3 and text.isdigit() and text[0] != "0"




def passport_ok(fields):
   """fields is a dictionary like {"byr": "1937", "hgt": "183cm", ...}"""
   for field in REQUIRED_FIELDS:
       if field not in fields:
           return False


   return (year_ok(fields["byr"], 1922, 2010)
           and year_ok(fields["iyr"], 2016, 2026)
           and year_ok(fields["eyr"], 2026, 2036)
           and height_ok(fields["hgt"])
           and hair_ok(fields["hcl"])
           and fields["ecl"] in EYE_COLORS
           and country_ok(fields["cid"]))




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
   fields = {}
   for line in passport:
       for pair in line.split():              # pairs are separated by spaces
           if ":" in pair:
               key, value = pair.split(":", 1)    # "byr:1937" -> "byr", "1937"
               fields[key] = value


   if passport_ok(fields):
       valid_passports.append(passport)


# ---------- Write the valid passports, one blank line between each ----------
with open("valid_passports2.txt", "w") as outfile:
   for index in range(len(valid_passports)):
       if index > 0:
           outfile.write("\n")
       for line in valid_passports[index]:
           outfile.write(line + "\n")


print(f"There are {len(valid_passports)} valid passports")
