import FreeCAD as App
from PySide import QtGui
import Part
import Sketcher
import csv

# create the FreeCAD document 
theDocument = App.newDocument()  
sketch = theDocument.addObject("Sketcher::SketchObject", "MacroSketch")

# the meat
theCircle = sketch.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theCircle}")
sketch.addConstraint(Sketcher.Constraint('Weight',0,1.000000))
sketch.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
# try to delete the circle

theCircle = sketch.addGeometry(Part.Circle(App.Vector(28.3069,4.7619,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theCircle}")
sketch.addConstraint(Sketcher.Constraint('Equal',0,1)) 
# try to delete the circle

theCircle = sketch.addGeometry(Part.Circle(App.Vector(49.7354,15.3439,0),App.Vector(0,0,1),10),True)
print(f"theCircle: {theCircle}")
sketch.addConstraint(Sketcher.Constraint('Equal',0,2)) 
# try to delete the circle

sketch.addGeometry(Part.BSplineCurve(
    [
        App.Vector(0,0),
        App.Vector(28.3069,4.7619),
        App.Vector(49.7354,15.3439)
    ],None,None,False,3,None,False),False)

conList = []
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,3,3,0))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,3,3,1))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,3,3,2))
del conList

sketch.exposeInternalGeometry(3)

"""
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Weight',0,1.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(7.555460,6.396178,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,1)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(24.025883,12.166837,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,2)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.Circle(App.Vector(43.501850,7.478178,0),App.Vector(0,0,1),10),True)
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,3)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.BSplineCurve([App.Vector(0,0),App.Vector(7.55546,6.39618),App.Vector(24.0259,12.1668),App.Vector(43.5019,7.47818)],None,None,False,3,None,False),False)
>>> conList = []
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',0,3,4,0))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',1,3,4,1))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,3,4,2))
>>> conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',3,3,4,3))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(conList)
>>> del conList
>>> 
>>> App.getDocument('Unnamed').getObject('Sketch').exposeInternalGeometry(4)
"""

