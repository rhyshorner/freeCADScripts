import FreeCAD as App
from PySide import QtGui
import Part
import Sketcher
import csv

#example of csv 
# 0,0,0
# 1,0.001,0
# 2,0.002,0
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
    # Step value of 3 to pick every third element
    return data[::rowNumberToKeep]

# create the FreeCAD document 
theDocument = App.newDocument()  

# add a sketch to the document
sketch = theDocument.addObject("Sketcher::SketchObject", "Sketch")

# get file through the user dialog
file_dialog = QtGui.QFileDialog()
csv_file_path = file_dialog.getOpenFileName()[0]
data = read_csv_file(csv_file_path)

#data = remove_every_third_row(data)
data = keep_only_every_nth_row(data, 50)

# file has been found and data exists
if(data != None):
    # example of data [[0.0, 0.0, 0.0], [1.0, 0.001, 0.0], [2.0, 0.002, 0.0]]
    # Extract data from file
    #data = read_csv_file('.\\plotDot.txt')

    # add the first point to the sketch
    #x1, y1, z1 = data[0]
    #x2, y2, z2 = data[1]
    #sketch.addGeometry(Part.LineSegment(App.Vector(x1, y1, z1), App.Vector(x2, y2, z2)), False)

    # foreach row in data (list of X Y Z coorindates)
    xPrevious, yPrevious, zPrevious = data[0]
    #lineNumber = sketch.GeometryCount
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

    # constrains the first lines ending vertex to the second lines starting vertex
    # sketch.addConstraint(Sketcher.Constraint("Coincident", 0, 2, 1, 1))
    # constrains the Seconds line's ending vertex to the Third line's starting vertex
    # sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 2, 1))
    """
    App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',0,2,1,1))
    """
