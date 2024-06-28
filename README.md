These are just some script's I created for myself to figure out how to use python in FreeCAD.


pip install freecad-stubs
https://wiki.freecad.org/Python_scripting_tutorial





theSecondCircle = Part.Circle(Center=FreeCAD.Vector(28.307,4.762,0), Normal=FreeCAD.Vector(0,0,1), Radius=10)
    Creates a Part.Circle object
paramter 1 (Center):
    location of the center of the circle
parameter 2 (Normal):
    
parameter 3 (radius):
    the radius of the circle

sketch.addGeometry(theSecondCircle, True)
parameter 1:
    is a Part.Circle object 
parameter 2: 
    bool, determines if geometry is a construction or not (True is construction geometry)




Sketcher.Constraint('Coincident',0,3,-1,1)
parameter 1:
    'Coincident': Refers to the constraint type
parameter 2:
    refers to the index of the first geometry entity involved in the constraint
parameter 3:
    refers to the index of the second geometry entity involved in the constraint
parameter 4 and 5:
    refers to specific points or sub-elements within the entities
        0: Refers to the Origin.
        -1: Refers to the horizontal axis (X-axis).
        -2: Refers to the vertical axis (Y-axis).