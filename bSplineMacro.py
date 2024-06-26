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


"""
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Weight',0,1.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(28.306892,4.761905,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,1)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(49.735443,15.343916,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,2)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(75.396828,35.185188,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,3)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(94.444435,16.137564,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,4)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(118.518509,5.555558,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,5)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(147.354492,0.000000,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,6)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',6,3,-1)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.BSplineCurve([App.Vector(0,0),App.Vector(28.3069,4.7619),App.Vector(49.7354,15.3439),App.Vector(75.3968,35.1852),App.Vector(94.4444,16.1376),App.Vector(118.519,5.55556),App.Vector(147.354,0)],None,None,False,3,None,False),False)
>>> conList = []
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,3,7,0))
0 is the point number, 3 is ?, 7 is the last point number+1, 0 is the current point number
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,3,7,1))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,3,7,2))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',3,3,7,3))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',4,3,7,4))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',5,3,7,5))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',6,3,7,6))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(conList)
>>> del conList
>>> 
>>> App.getDocument('Unnamed').getObject('Sketch').exposeInternalGeometry(7)
"""

