import xml.etree.ElementTree as ET
import yaml

# Parse the input XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Extract the required information from the XML
job_name = root.attrib['Name']
job_desc = root.attrib['Desc']
job_status = root.attrib['Status']
job_wave_no = root.attrib['WaveNo']
job_start_date_time = root.attrib['StartDateTime']
job_end_date_time = root.attrib['EndDateTime']
job_elapsed_time = root.attrib['ElapsedTime']
job_elapsed_secs = root.attrib['ElapsedSecs']

params = []
for param in root.find('ParamSet').findall('Param'):
    param_dict = {
        'Name': param.attrib['Name'],
        'Type': param.attrib['Type'],
        'Desc': param.attrib['Desc'],
        'Value': param.attrib['Value']
    }
    params.append(param_dict)

stages = []
for stage in root.find('ComponentSet').findall('Stage'):
    stage_dict = {
        'Name': stage.attrib['Name'],
        'StageStatus': stage.attrib['StageStatus'],
        'StageType': stage.attrib['StageType'],
        'Desc': stage.attrib['Desc'],
        'StartDateTime': stage.attrib['StartDateTime'],
        'EndDateTime': stage.attrib['EndDateTime'],
        'ElapsedTime': stage.attrib['ElapsedTime'],
        'ElapsedSecs': stage.attrib['ElapsedSecs'],
        'OutputLinks': []
    }
    for link in stage.find('OutputLinks').findall('Link'):
        link_dict = {
            'Name': link.attrib['Name'],
            'LinkType': link.attrib['LinkType'],
            'Desc': link.attrib['Desc'],
            'Stage': link.attrib['Stage']
        }
        stage_dict['OutputLinks'].append(link_dict)
    stages.append(stage_dict)

# Create a dictionary for the output YAML file
output_dict = {
    'Job': {
        'Name': job_name,
        'Desc': job_desc,
        'Status': job_status,
        'WaveNo': job_wave_no,
        'StartDateTime': job_start_date_time,
        'EndDateTime': job_end_date_time,
        'ElapsedTime': job_elapsed_time,
        'ElapsedSecs': job_elapsed_secs,
        'ParamSet': params,
        'ComponentSet': stages
    }
}

# Write the output YAML file
with open('output.yml', 'w') as file:
    yaml.dump(output_dict, file)
