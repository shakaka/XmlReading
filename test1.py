import xml.etree.ElementTree as ET
import xmltodict
import json, os

path = os.getcwd()
files = os.listdir('samples')
# print(files)

files_xml = [f for f in files if f[-4:] == '.xml']
# print(files_xml)

for f in files_xml:
    file_name = f
    tree = ET.parse('samples/GU20404050_20210121021121083.xml')
    xml_data = tree.getroot()
    xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')

    data_dict = dict(xmltodict.parse(xmlstr))
    # print(data_dict)
    # print (json.dumps(data_dict, sort_keys=True, indent=4))
    # print (data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:account', {}).get('ns0:mRID'))
    account = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:account', {}).get('ns0:mRID')
    spdID = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:serviceLocation', {}).get('ns0:mRID')
    badgeID = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:badgeId')
    # print(badgeID)
    # print(data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter'))
    contractType = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[0].get('ns0:value')
    recContrctType = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[1].get('ns0:value')
