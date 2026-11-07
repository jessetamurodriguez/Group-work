# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Yulian Villarreal
# Section:      102 M02
# Assignment:   Lab 11 (individual)
# Date:         6/11/2026
OUTPUT_FILE = "valid_barcodes.txt"
def is_valid(barcode):
    """Return True when the 13th digit matches the computed check digit."""
    if len(barcode) != 13 or not barcode.isdigit():
        return False
    first_group = barcode[0:12:2]     # digits 1, 3, 5, 7, 9, 11
    second_group = barcode[1:12:2]    # digits 2, 4, 6, 8, 10, 12
    first_sum = 0
    for digit in first_group:
        first_sum = first_sum + int(digit)
    second_sum = 0
    for digit in second_group:
        second_sum = second_sum + int(digit)
    total = first_sum + second_sum * 3
    check_digit = 10 - (total % 10)
    if check_digit == 10:             # a total that ends in zero
        check_digit = 0
    return check_digit == int(barcode[-1])
def main():
    filename = input("Enter the name of the file: ")
    valid = []
    with open(filename, "r") as infile:
        for line in infile:
            barcode = line.strip()
            if barcode != "" and is_valid(barcode):
                valid.append(barcode)
    with open(OUTPUT_FILE, "w") as outfile:
        for barcode in valid:
            print(barcode, file=outfile)
    print("There are", len(valid), "valid barcodes")
main()