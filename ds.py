import xml.etree.ElementTree as ET

# Specify the path to the Control-M parent folder job XML file
xml_file = "path/to/xml/file.xml"

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Loop through each job in the XML file
for job in root.findall(".//Job[@parentfoldername]"):
    # Get the job name and print it
    job_name = job.attrib['name']
    print(f"Job name: {job_name}")
    
    # Get the job parameters and print them
    for param in job.findall(".//Parameter"):
        param_name = param.attrib['name']
        param_value = param.attrib['value']
        print(f"\tParameter name: {param_name}")
        print(f"\tParameter value: {param_value}")
