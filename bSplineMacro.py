import FreeCAD as App
from PySide import QtGui
import Part
import Sketcher
import csv

def read_csv_file(filename):
    data = []  # List to store arrays of floats
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    float_row = [float(value) for value in row]  # Convert each value to a float
                    data.append(float_row)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("Error, Cannot find file.")
        return None
    return data

def keep_only_every_nth_row(data, rowNumberToKeep):
    return data[::rowNumberToKeep]

# create the FreeCAD document 
theDocument = App.newDocument()  

# add a sketch to the document
sketch = theDocument.addObject("Sketcher::SketchObject", "MacroSketch")

# get file through the user dialog
file_dialog = QtGui.QFileDialog()
csv_file_path = file_dialog.getOpenFileName()[0]
data = read_csv_file(csv_file_path)

data = keep_only_every_nth_row(data, 50)

# begin the meat
if(data != None):
    xPrevious, yPrevious, zPrevious = data[0]
    firstLoop = True
    for row in data:
        if(not firstLoop):
            x, y, z = row
            print(f"from:{xPrevious, yPrevious, zPrevious} to:{row}")
            sketch.addGeometry(Part.LineSegment(App.Vector(xPrevious, yPrevious, zPrevious), App.Vector(x, y, z)), False)
            sketch.addConstraint(Sketcher.Constraint("Coincident", sketch.GeometryCount-2, 2, sketch.GeometryCount-1, 1))
            x_axis = -2
            sketch.addConstraint(Sketcher.Constraint('Distance',sketch.GeometryCount-1,2,x_axis,x))
            y_axis = -1
            sketch.addConstraint(Sketcher.Constraint('Distance',sketch.GeometryCount-1,2,y_axis,y))
            xPrevious, yPrevious, zPrevious = row
        firstLoop = False

    theDocument.recompute()