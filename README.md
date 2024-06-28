These are just some script's I created for myself to figure out how to use python in FreeCAD.


pip install freecad-stubs
https://wiki.freecad.org/Python_scripting_tutorial





theSecondCircle = Part.Circle(Center=FreeCAD.Vector(28.307,4.762,0), Normal=FreeCAD.Vector(0,0,1), Radius=10)
    Creates a Part.Circle object
paramter 1 (Center):
    location of the center of the circle
parameter 2 (Normal):
    Specifies the orientation of the circle, (0,0,1) means the circle lies in the XY plane with its center at the origin and its normal vector pointing in the positive Z direction
parameter 3 (radius):
    the radius of the circle

sketch.addGeometry(theSecondCircle, True)
parameter 1:
    is a Part object 
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

b = Part.BSplineCurve([
    FreeCAD.Vector(0, 0),
    FreeCAD.Vector(28.307, 4.762),
    FreeCAD.Vector(49.735, 15.344),
    FreeCAD.Vector(75, 5)
], None, None, False, 3, None, False)
parameter 1: 
    a list of control points. In your example, these are the vectors (0, 0), (28.307, 4.762), (49.735, 15.344), and (75, 5).
parameter 2: 
    the knot vector. Since it’s set to None, the constructor will generate a uniform knot vector automatically.
parameter 3: 
    the multiplicity vector. Again, it’s set to None, so the constructor will compute it based on the degree of the curve.
parameter 4: 
    (False) specifies whether the curve is closed. In your case, it’s not a closed curve.
parameter:
    The fifth argument (3) represents the degree of the B-spline curve. Higher degrees allow more flexibility in shaping the curve.
parameter:
    The sixth argument is the parameter range. Since it’s set to None, the constructor will use the default parameter range.
parameter:
    The seventh argument (False) determines whether the curve is periodic. For your example, it’s not periodic.
In summary, your b object represents a B-spline curve defined by the given control points, with a degree of 3, and it’s not closed or periodic