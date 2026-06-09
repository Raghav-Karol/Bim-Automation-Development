import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document

beams_bucket = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()

print("=" * 75)
headers = "BEAM ID".ljust(12) + "VOLUME (m3)".ljust(15) + "MATERIAL AUDIT STATUS"
print(headers)
print("-" * 75)

for beam in beams_bucket:
    beam_id = str(beam.Id)
    material_id = beam.StructuralMaterialId
    vol_param = beam.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED)
    
    if vol_param:
        raw_m3 = vol_param.AsDouble() / 35.3147
        vol_m3 = str(round(raw_m3, 2))
    else:
        vol_m3 = "0.0"
        
    if material_id == ElementId.InvalidElementId:
        status = "🚨 CRITICAL: Missing Material Asset Pointer!"
    else:
        status = "✅ PASSED: Structural Schema Valid"
        
    row_layout = beam_id.ljust(12) + vol_m3.ljust(15) + status
    print(row_layout)

print("=" * 75)