import csv

#example of csv 
# 0,0,0
# 1,0.001,0
# 2,0.002,0
def read_csv_file(filename):
    data = []  # List to store arrays of doubles
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    double_row = [float(value) for value in row]  # Convert each value to a float
                    data.append(double_row)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("Error, Cannot find file.")
    return data

#Main
# example of data [[0.0, 0.0, 0.0], [1.0, 0.001, 0.0], [2.0, 0.002, 0.0]]
data = read_csv_file('.\\plotDot.txt')

# printing all the rows of data, for debugging
for row in data:
    x, y, z = row
    print(f"{x},{y},{z}")  # List of arrays, each containing three doubles