# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Yulian Villarreal
# Section:      102 M02
# Assignment:   Lab 11 (individual)
# Date:         6/11/2026
import csv
from datetime import datetime
FILE_NAME = "WeatherDataCLL.csv"
# Each column is looked up by keyword, so the program still works when the
# headers in the file are worded a little differently.
COLUMN_KEYWORDS = {
    "date": [("date",)],
    "max_temp": [("max", "temp")],
    "min_temp": [("min", "temp")],
    "wet_bulb": [("wet",)],
    "dew_point": [("dew",)],
    "average_temp": [("average", "temp"), ("temp",)],
    "pressure": [("average", "pressure"), ("pressure",)],
    "humidity": [("average", "humidity"), ("humidity",)],
    "wind_speed": [("average", "wind"), ("wind",)],
    "precipitation": [("precip",)],
}
DATE_FORMATS = ("%m/%d/%Y", "%m/%d/%y", "%Y-%m-%d", "%m/%d/%Y %H:%M")
def find_column(headers, keyword_sets, used):
    """Return the first unused header that contains every keyword."""
    for keywords in keyword_sets:
        for header in headers:
            if header in used:
                continue
            name = header.strip().lower()
            if all(keyword in name for keyword in keywords):
                return header
    return None
def to_float(text):
    """Turn a cell into a float, or None when that day is missing data."""
    text = text.strip()
    if text == "":
        return None
    try:
        return float(text)
    except ValueError:
        return None
def parse_date(text):
    """Turn the date cell into a datetime using the usual formats."""
    for pattern in DATE_FORMATS:
        try:
            return datetime.strptime(text.strip(), pattern)
        except ValueError:
            continue
    return None
def column_values(rows, column):
    """Every number in one column, skipping the days with no reading."""
    if column is None:
        return []
    values = []
    for row in rows:
        value = to_float(row[column])
        if value is not None:
            values.append(value)
    return values
def mean(values): # Calculate the average of a list of numbers
    """Average a list of numbers, or None when the list is empty."""
    if len(values) == 0:
        return None
    return sum(values) / len(values)
def month_matches(day, month_name): # Match a full month name or just its first three letters
    """Match a full month name or just its first three letters."""
    wanted = month_name.strip().lower()
    if len(wanted) < 3:
        return False
    return day.strftime("%B").lower().startswith(wanted[:3])
def show(label, value, decimals, unit): # Print one monthly result, or say so when the month has no data
    """Print one monthly result, or say so when the month has no data."""
    if value is None:
        print(label + ": no data")
    else:
        print(label + ": " + format(value, "." + str(decimals) + "f") + unit)
def main(): # Main function to run the weather data analysis
    with open(FILE_NAME) as infile:
        reader = csv.DictReader(infile)
        headers = reader.fieldnames
        rows = list(reader)
    columns = {}
    used = []
    order = ["date", "max_temp", "min_temp", "wet_bulb", "dew_point",
             "average_temp", "pressure", "humidity", "wind_speed",
             "precipitation"]
    for key in order:
        column = find_column(headers, COLUMN_KEYWORDS[key], used)
        columns[key] = column
        if column is not None:
            used.append(column)
    highs = column_values(rows, columns["max_temp"])
    if len(highs) == 0:
        highs = column_values(rows, columns["average_temp"])
    lows = column_values(rows, columns["min_temp"])
    if len(lows) == 0:
        lows = column_values(rows, columns["average_temp"])
    if len(highs) == 0 or len(lows) == 0 or columns["date"] is None:
        print("The headers in", FILE_NAME, "did not look right.")
        return
    print("10-year maximum temperature:", format(max(highs), "g"), "F")
    print("10-year minimum temperature:", format(min(lows), "g"), "F")
    print()
    month_name = input("Please enter a month: ")
    year = int(input("Please enter a year: "))
    month_rows = []
    for row in rows:
        day = parse_date(row[columns["date"]])
        if day is None:
            continue
        if day.year == year and month_matches(day, month_name):
            month_rows.append(row)
    print()
    print("For " + month_name.strip().capitalize() + " " + str(year) + ":")
    show("Mean average daily pressure",
         mean(column_values(month_rows, columns["pressure"])), 2, " in Hg")
    show("Mean average daily temperature",
         mean(column_values(month_rows, columns["average_temp"])), 1, " F")
    show("Mean average daily wet bulb temperature",
         mean(column_values(month_rows, columns["wet_bulb"])), 1, " F")
    show("Mean average daily dew point",
         mean(column_values(month_rows, columns["dew_point"])), 1, " F")
    show("Mean average daily relative humidity",
         mean(column_values(month_rows, columns["humidity"])), 1, "%")
    show("Mean average daily wind speed",
         mean(column_values(month_rows, columns["wind_speed"])), 2, " mph")
    precipitation = column_values(month_rows, columns["precipitation"])
    wet_days = 0
    for value in precipitation:
        if value > 0:
            wet_days = wet_days + 1
    if len(precipitation) == 0:
        print("Percentage of days with precipitation: no data")
    else:
        percent = wet_days / len(precipitation) * 100
        print("Percentage of days with precipitation: "
              + format(percent, ".1f") + "%")
main()