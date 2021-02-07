import xml.etree.ElementTree as ET
import xmltodict
import json, os

path = os.getcwd()
files = os.listdir('samples')
# print(files)
fileOut = open("output","a")
files_xml = [f for f in files if f[-4:] == '.xml']
# print(files_xml)

for f in files_xml:
    file_name = f
    tree = ET.parse('samples/'+f)
    xml_data = tree.getroot()
    xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')

    data_dict = dict(xmltodict.parse(xmlstr))
    # print(data_dict)
    # print (json.dumps(data_dict, sort_keys=True, indent=4))
    # print (data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:account', {}).get('ns0:mRID'))
    account = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:account', {}).get('ns0:mRID')
    spdID = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:mRID')
    badgeID = data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:badgeId')
    # print(badgeID)
    # print(data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter'))
    contractType =      data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[0].get('ns0:value')
    recConType =    data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[1].get('ns0:value')

    section =       {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[2].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[2].get('ns0:value')}
    region =        {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[3].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[3].get('ns0:value')}
    publishType =   {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[4].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[4].get('ns0:value')}
    multipleSDP =   {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[5].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:servicePoint', {}).get('ns0:parameter')[5].get('ns0:value')}

    installType =   {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[0].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[0].get('ns0:value')}
    refElecNum =    {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[1].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[1].get('ns0:value')}
    dials =         {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[2].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[2].get('ns0:value')}
    programID =     {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[3].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[3].get('ns0:value')}
    demandUser =    {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[4].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[4].get('ns0:value')}
    withReactive =  {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[5].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[5].get('ns0:value')}
    voltageType =   {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[6].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[6].get('ns0:value')}
    phase =         {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[7].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[7].get('ns0:value')}
    direction =     {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[8].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[8].get('ns0:value')}
    hesName =       {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[9].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[9].get('ns0:value')}
    billingD =      data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[10].get('ns0:value')
    recBillingD =   data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[11].get('ns0:value')
    usCon =         {data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[12].get('ns0:name'):data_dict.get('ns0:SDPSyncMessage', {}).get('ns0:payload', {}).get('ns0:device', {})[0].get('ns0:parameter')[12].get('ns0:value')}

    sps = [section, region, publishType, multipleSDP]
    devs = [installType, refElecNum, dials, programID, demandUser, withReactive, voltageType, phase, direction, hesName, hesName, usCon]
    devNs = [dials, programID, voltageType, phase, direction, hesName]

    fileOut.write(str(f)+','+str(account)+','+str(badgeID)+','+str(spdID)+',')

    for sp in sps:
        if list(sp.values())[0] == None or list(sp.values())[0] =='null':
            sp = list(sp.keys())[0]+' is null/empty. '
            fileOut.write(sp)
        else: sp = ''
    for dev in devs:
        if list(dev.values())[0] == None:
            dev = list(dev.keys())[0]+' is empty. '
            fileOut.write(dev)
        else: dev = ''
    for devN in devNs:
        if list(devN.values())[0] == 'null':
            devN = list(devN.keys())[0]+' is null. '
            fileOut.write(devN)
        else: devN = ''

    if contractType =='null' and recConType == 'null':
        contract = 'ContractType are both null. '
        fileOut.write(contract)
    if billingD =='null' and recBillingD == 'null':
        billing = 'Billing are both null. '
        fileOut.write(billing)

    fileOut.write('\n')

fileOut.close()
