import xml.etree.ElementTree as ET
import yaml

# Read input XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Parse XML data and create Python dictionary
job_dict = {}
job_dict['Job'] = {}
job_dict['Job']['Name'] = root.attrib['Name']
job_dict['Job']['Desc'] = root.attrib['Desc']
job_dict['Job']['Status'] = root.attrib['Status']
job_dict['Job']['WaveNo'] = root.attrib['WaveNo']
job_dict['Job']['StartDateTime'] = root.attrib['StartDateTime']
job_dict['Job']['EndDateTime'] = root.attrib['EndDateTime']
job_dict['Job']['ElapsedTime'] = root.attrib['ElapsedTime']
job_dict['Job']['ElapsedSecs'] = root.attrib['ElapsedSecs']
job_dict['Job']['Params'] = {}
for param in root.findall('.//Param'):
    param_dict = {}
    param_dict['Type'] = param.attrib['Type']
    param_dict['Desc'] = param.attrib['Desc']
    param_dict['Value'] = param.attrib['Value']
    job_dict['Job']['Params'][param.attrib['Name']] = param_dict
job_dict['Job']['Stages'] = {}
for stage in root.findall('.//Stage'):
    stage_dict = {}
    stage_dict['Name'] = stage.attrib['Name']
    stage_dict['StageStatus'] = stage.attrib['StageStatus']
    stage_dict['StageType'] = stage.attrib['StageType']
    stage_dict['Desc'] = stage.attrib['Desc']
    stage_dict['StartDateTime'] = stage.attrib['StartDateTime']
    stage_dict['EndDateTime'] = stage.attrib['EndDateTime']
    stage_dict['ElapsedTime'] = stage.attrib['ElapsedTime']
    stage_dict['ElapsedSecs'] = stage.attrib['ElapsedSecs']
    stage_dict['InputLinks'] = {}
    for input_link in stage.findall('.//InputLinks/Link'):
        input_link_dict = {}
        input_link_dict['LinkType'] = input_link.attrib['LinkType']
        input_link_dict['Desc'] = input_link.attrib['Desc']
        input_link_dict['Stage'] = input_link.attrib['Stage']
        stage_dict['InputLinks'][input_link.attrib['Name']] = input_link_dict
    stage_dict['OutputLinks'] = {}
    for output_link in stage.findall('.//OutputLinks/Link'):
        output_link_dict = {}
        output_link_dict['LinkType'] = output_link.attrib['LinkType']
        output_link_dict['Desc'] = output_link.attrib['Desc']
        output_link_dict['Stage'] = output_link.attrib['Stage']
        stage_dict['OutputLinks'][output_link.attrib['Name']] = output_link_dict
    stage_dict['Instances'] = {}
    for instance in stage.findall('.//InstanceSet/Instance'):
        instance_dict = {}
        instance_dict['CPU'] = instance.attrib['CPU']
        instance_dict['PID'] = instance.attrib['PID']
        instance_dict['InputLinks'] = {}
        for input_link in instance.findall('.//Link'):
            input_link_dict = {}
            input_link_dict['RowCount'] = input_link.attrib['RowCount']
            instance_dict['InputLinks'][input_link.attrib['Name']] = input_link_dict
        stage_dict['Instances'][instance.attrib['Id']] = instance_dict
    job_dict['Job']['Stages'][stage.attrib['Name']] = stage_dict

# Write Python dictionary to output YAML file
with open('output.yml', 'w') as outfile:
    yaml.dump(job_dict, outfile, default_flow_style=False)
