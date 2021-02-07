import xml.etree.ElementTree as ET

tree = ET.parse("samples\XDFExport_SS.xml")
root = tree.getroot()
n1=0
n2=0
n3=0
# print (root.tag)
# print (root.attrib)
#
# for child in root:
#     print(child.tag, child.attrib)
# print (root[0][0][0][2].get('Name'))
# for v in root.find('Instances').find('Parent').find('SubGeographicalRegion').find('Substation'):
#     print (v.get('Name'))
# print( root.findall("./Instances/Parent/SubGeographicalRegion/Substation"))
# for busbar in root.findall("./Instances/Parent/SubGeographicalRegion/Substation/VoltageLevel/BusbarSection"):
#     # print (v.get('Name'))
#     if "BUS" not in busbar.get('Name'):
#         print(busbar.get('Name'))
#         root.find('Instances').find('Parent').find('SubGeographicalRegion').find('Substation').find('VoltageLevel').remove(busbar)
#         #root.find('Instances').find('Parent').find('SubGeographicalRegion').find('Substation').find('VoltageLevel').find('BusbarSection').remove(busbar)
# tree.writeET("samples\XDFExport_SS_new.xml")
for a in root.findall("./Instances/Parent/SubGeographicalRegion/Substation"):
    n1=n1+1
for a in root.findall("./Instances/Parent/SubGeographicalRegion/Substation/VoltageLevel"):
    n2=n2+1
for a in root.findall("./Instances/Parent/SubGeographicalRegion/Substation/VoltageLevel/BusbarSection"):
    n3=n3+1

print (n1)
print (n2)
print (n3)
