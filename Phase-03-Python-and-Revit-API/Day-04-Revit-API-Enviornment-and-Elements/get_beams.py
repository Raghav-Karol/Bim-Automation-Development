import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document

beams_bucket = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
print(len(beams_bucket))

first_beam = beams_bucket[0]
vol_param = first_beam.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED)
print(vol_param.AsDouble())