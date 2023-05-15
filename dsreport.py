import xml.etree.ElementTree as ET
import yaml

# Parse XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Create dictionary to store job details
job_details = {}
job_details['Job'] = {}
job_details['Job']['Name'] = root.attrib['Name']
job_details['Job']['Desc'] = root.attrib['Desc']
job_details['Job']['Status'] = root.attrib['Status']
job_details['Job']['WaveNo'] = root.attrib['WaveNo']
job_details['Job']['StartDateTime'] = root.attrib['StartDateTime']
job_details['Job']['EndDateTime'] = root.attrib['EndDateTime']
job_details['Job']['ElapsedTime'] = root.attrib['ElapsedTime']
job_details['Job']['ElapsedSecs'] = root.attrib['ElapsedSecs']

# Create list to store parameter details
param_list = []
for param in root.findall("./ParamSet/Param"):
    param_dict = {}
    param_dict['Name'] = param.attrib['Name']
    param_dict['Type'] = param.attrib['Type']
    param_dict['Desc'] = param.attrib['Desc']
    param_dict['Value'] = param.attrib['Value']
    param_list.append(param_dict)

job_details['ParamSet'] = param_list

# Create list to store stage details
stage_list = []
for stage in root.findall("./ComponentSet/Stage"):
    stage_dict = {}
    stage_dict['Name'] = stage.attrib['Name']
    stage_dict['StageStatus'] = stage.attrib['StageStatus']
    stage_dict['StageType'] = stage.attrib['StageType']
    stage_dict['Desc'] = stage.attrib['Desc']
    stage_dict['StartDateTime'] = stage.attrib['StartDateTime']
    stage_dict['EndDateTime'] = stage.attrib['EndDateTime']
    stage_dict['ElapsedTime'] = stage.attrib['ElapsedTime']
    stage_dict['ElapsedSecs'] = stage.attrib['ElapsedSecs']
    
    # Create list to store input link details
    input_links = []
    for link in stage.findall("./InputLinks/Link"):
        link_dict = {}
        link_dict['Name'] = link.attrib['Name']
        link_dict['LinkType'] = link.attrib['LinkType']
        link_dict['Desc'] = link.attrib['Desc']
        link_dict['Stage'] = link.attrib['Stage']
        input_links.append(link_dict)
    
    stage_dict['InputLinks'] = input_links
    
    # Create list to store output link details
    output_links = []
    for link in stage.findall("./OutputLinks/Link"):
        link_dict = {}
        link_dict['Name'] = link.attrib['Name']
        link_dict['LinkType'] = link.attrib['LinkType']
        link_dict['Desc'] = link.attrib['Desc']
        link_dict['Stage'] = link.attrib['Stage']
        output_links.append(link_dict)
    
    stage_dict['OutputLinks'] = output_links
    
    stage_list.append(stage_dict)

job_details['ComponentSet'] = stage_list

# Output YAML file
with open('output.yml', 'w') as outfile:
    yaml.dump(job_details, outfile, default_flow_style=False)
