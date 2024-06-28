import FreeCAD
from PySide import QtGui
import Part
import Sketcher
import csv

# need to add many constraints to complete the spline properly, 
# - need x and y axis for the circles
# - need circle to control point coincidence constraints
# - need the begining circle to coincide with the origin


# create the FreeCAD document 
theDocument = FreeCAD.newDocument()  
sketch = theDocument.addObject("Sketcher::SketchObject", "MacroSketch")

# the meat
"""The first loop"""
theFirstCircle = Part.Circle(FreeCAD.Vector(0.000000,0.000000,0),FreeCAD.Vector(0,0,1),10)
theID = sketch.addGeometry(theFirstCircle, True)
print(f"theGeometryID:{theID}")
# theID = sketch.addConstraint(Sketcher.Constraint('Weight',0,1.000000))
# print(f"theWeightConstraint: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
print(f"theConstraint: {theID}")

"""The second loop"""
theSecondCircle = Part.Circle(Center=FreeCAD.Vector(28.307,4.762,0), Normal=FreeCAD.Vector(0,0,1), Radius=10)
theID = sketch.addGeometry(theSecondCircle, True)
print(f"theCircle: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Equal',0,1)) 
print(f"theConstraint: {theID}")

"""The third loop"""
theID = sketch.addGeometry(Part.Circle(FreeCAD.Vector(49.7354,15.344,0),FreeCAD.Vector(0,0,1),10),True)
print(f"theCircle: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
print(f"theConstraint: {theID}") 

"""The final loop"""
theID = sketch.addGeometry(Part.Circle(FreeCAD.Vector(75,5,0),FreeCAD.Vector(0,0,1),10),True)
print(f"theCircle: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Equal',0,3))
print(f"theConstraint: {theID}") 

# create the bspline and then add the geometry
b = Part.BSplineCurve([
    FreeCAD.Vector(0, 0),
    FreeCAD.Vector(28.307, 4.762),
    FreeCAD.Vector(49.735, 15.344),
    FreeCAD.Vector(75, 5)
], None, None, False, 3, None, False)
sketch.addGeometry(b, False)
theDocument.recompute()

print(f"object:{b}, startPoint:{b.StartPoint}, endpoint:{b.EndPoint}")
theDocument.recompute()

conList = []
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,4,3,0))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,4,3,1))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,4,3,2))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',3,4,3,3))
del conList

sketch.exposeInternalGeometry(4)
theDocument.recompute()
'''
theDocument = App.newDocument()  
sketch = theDocument.addObject("Sketcher::SketchObject", "MacroSketch")

# the meat
"""The first loop"""
theID = sketch.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theID}")
# theID = sketch.addConstraint(Sketcher.Constraint('Weight',0,1.000000))
# print(f"theWeightConstraint: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
print(f"theConstraint: {theID}")

"""The second loop"""
theID = sketch.addGeometry(Part.Circle(App.Vector(28.307,4.762,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Equal',0,1)) 
print(f"theConstraint: {theID}")

"""The third loop"""
theID = sketch.addGeometry(Part.Circle(App.Vector(49.7354,15.344,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Equal',0,2))
print(f"theConstraint: {theID}") 

"""The final loop"""
theID = sketch.addGeometry(Part.Circle(App.Vector(75,5,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theID}")
theID = sketch.addConstraint(Sketcher.Constraint('Equal',0,3))
print(f"theConstraint: {theID}") 

# create the bspline and then add the geometry
b = Part.BSplineCurve([
    App.Vector(0, 0),
    App.Vector(28.307, 4.762),
    App.Vector(49.735, 15.344),
    App.Vector(75, 5)
], None, None, False, 3, None, False)
sketch.addGeometry(b, False)
print(f"object:{b}, startPoint:{b.StartPoint}, endpoint:{b.EndPoint}")

conList = []
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,4,3,0))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,4,3,1))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,4,3,2))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',3,4,3,3))
del conList

sketch.exposeInternalGeometry(4)

'''