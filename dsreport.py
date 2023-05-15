import xml.etree.ElementTree as ET
import yaml

# read the input XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# extract job details
job = {}
job['Name'] = root.attrib['Name']
job['Desc'] = root.attrib['Desc']
job['Status'] = root.attrib['Status']
job['WaveNo'] = root.attrib['WaveNo']
job['StartDateTime'] = root.attrib['StartDateTime']
job['EndDateTime'] = root.attrib['EndDateTime']
job['ElapsedTime'] = root.attrib['ElapsedTime']
job['ElapsedSecs'] = root.attrib['ElapsedSecs']

# extract parameter details
params = []
for param in root.iter('Param'):
    param_dict = {}
    param_dict['Name'] = param.attrib['Name']
    param_dict['Type'] = param.attrib['Type']
    param_dict['Desc'] = param.attrib['Desc']
    param_dict['Value'] = param.attrib['Value']
    params.append(param_dict)

# extract stage details
stages = []
for stage in root.iter('Stage'):
    stage_dict = {}
    stage_dict['Name'] = stage.attrib['Name']
    stage_dict['Desc'] = stage.attrib['Desc']
    stage_dict['StageStatus'] = stage.attrib['StageStatus']
    stage_dict['StageType'] = stage.attrib['StageType']
    stage_dict['StartDateTime'] = stage.attrib['StartDateTime']
    stage_dict['EndDateTime'] = stage.attrib['EndDateTime']
    stage_dict['ElapsedTime'] = stage.attrib['ElapsedTime']
    stage_dict['ElapsedSecs'] = stage.attrib['ElapsedSecs']

    # extract input link details
    input_links = []
    for input_link in stage.iter('Link'):
        if input_link.attrib['LinkType'] == '1':
            input_link_dict = {}
            input_link_dict['Name'] = input_link.attrib['Name']
            input_link_dict['LinkType'] = input_link.attrib['LinkType']
            input_link_dict['Desc'] = input_link.attrib['Desc']
            input_link_dict['Stage'] = input_link.attrib['Stage']
            input_links.append(input_link_dict)

    # extract output link details
    output_links = []
    for output_link in stage.iter('Link'):
        if output_link.attrib['LinkType'] == '3':
            output_link_dict = {}
            output_link_dict['Name'] = output_link.attrib['Name']
            output_link_dict['LinkType'] = output_link.attrib['LinkType']
            output_link_dict['Desc'] = output_link.attrib['Desc']
            output_link_dict['Stage'] = output_link.attrib['Stage']
            output_links.append(output_link_dict)

    stage_dict['InputLinks'] = input_links
    stage_dict['OutputLinks'] = output_links

    stages.append(stage_dict)

# construct the YAML output
output = {}
output['Job'] = job
output['Params'] = params
output['Stages'] = stages

# write the output YAML file
with open('output.yml', 'w') as file:
    yaml.dump(output, file, default_flow_style=False)
