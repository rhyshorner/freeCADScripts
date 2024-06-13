import Draft
shape = App.ActiveDocument.ActiveObject.Shape

for w in shape.Wires:
    o=Draft.makeWire(w)
    o.ViewObject.DisplayMode="Wireframe"


    # dimensions accepted in format "40x50 mm" or "40 x 50 cm" or "40 50 cm"

import csv
import re
import FreeCAD
import Draft
from PySide import QtGui

def parse_dimensions(size):
    """
    input a string and return a number according to the given dimension
    """
    str_list = re.split('x| ', size)
    return_list = []
    u = 1
    for t in str_list:
        if t.isnumeric():
            return_list.append(float(t))
        else:
            if FreeCAD.Units.Quantity(t).Value > 1: u=FreeCAD.Units.Quantity(t).Value
    if len(return_list) == 0: return None
    if len(return_list) == 1: return return_list[0]*u, None, None,1
    if len(return_list) == 2: return return_list[0]*u,return_list[1]*u, None,2
    if len(return_list) == 3: return return_list[0]*u,return_list[1]*u,return_list[2]*u,3


def create_geometry(code=None, description=None, size=None):
    """
    creates the geometry in the document
    """

    print(code, description, size)
    w,l,h,dummy_type = parse_dimensions(size)
    print(w,l,h)
    if dummy_type == 2:
        r = Draft.makeRectangle(w,l)
        r.Label = code
        r.Label2 = description


# everything starts here
file_dialog = QtGui.QFileDialog()
csv_file_path = file_dialog.getOpenFileName()[0]
print("\nImporting: "+csv_file_path+"\n")

# this read the csv
with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        # for the first row print the headers
        if line_count == 0:
            print(f'Keys are: {", ".join(row)}\n')
            line_count += 1
        # for other rows extract the information
        code = row["codice"]
        description = row["titolo"]
        size = row["dimensioni_opera"]
        # and create the geometry
        create_geometry(code, description, size)
        line_count += 1

    print(f'\nProcessed {line_count} lines.\n')