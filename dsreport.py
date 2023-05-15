import xml.etree.ElementTree as ET
import yaml

# Load XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Initialize YAML data
yaml_data = {}

# Parse job information
job_info = {}
job_info['Name'] = root.attrib['Name']
job_info['Desc'] = root.attrib['Desc']
job_info['Status'] = root.attrib['Status']
job_info['WaveNo'] = root.attrib['WaveNo']
job_info['StartDateTime'] = root.attrib['StartDateTime']
job_info['EndDateTime'] = root.attrib['EndDateTime']
job_info['ElapsedTime'] = root.attrib['ElapsedTime']
job_info['ElapsedSecs'] = root.attrib['ElapsedSecs']
yaml_data['Job'] = job_info

# Parse stage information
stage_list = []
for component in root.findall('ComponentSet/Stage'):
    stage_info = {}
    stage_info['Name'] = component.attrib['Name']
    stage_info['StageStatus'] = component.attrib['StageStatus']
    stage_info['StageType'] = component.attrib['StageType']
    stage_info['Desc'] = component.attrib['Desc']
    stage_info['StartDateTime'] = component.attrib['StartDateTime']
    stage_info['EndDateTime'] = component.attrib['EndDateTime']
    stage_info['ElapsedTime'] = component.attrib['ElapsedTime']
    stage_info['ElapsedSecs'] = component.attrib['ElapsedSecs']

    # Parse input link information
    input_link_list = []
    for input_link in component.findall('InputLinks/Link'):
        if input_link.get('LinkType') == '1':
            input_link_info = {}
            input_link_info['Name'] = input_link.attrib['Name']
            input_link_info['Desc'] = input_link.attrib['Desc']
            input_link_info['Stage'] = input_link.attrib['Stage']
            input_link_list.append(input_link_info)
    stage_info['InputLinks'] = input_link_list

    # Parse output link information
    output_link_list = []
    for output_link in component.findall('OutputLinks/Link'):
        output_link_info = {}
        output_link_info['Name'] = output_link.attrib['Name']
        output_link_info['Desc'] = output_link.attrib['Desc']
        output_link_info['Stage'] = output_link.attrib['Stage']
        output_link_list.append(output_link_info)
    stage_info['OutputLinks'] = output_link_list

    # Append stage information to list
    stage_list.append(stage_info)

# Add stage information to YAML data
yaml_data['Stage'] = stage_list

# Output YAML data to file
with open('output.yml', 'w') as f:
    yaml.dump(yaml_data, f, default_flow_style=False)
