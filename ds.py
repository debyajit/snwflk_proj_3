# Import the xml.etree.ElementTree module
import xml.etree.ElementTree as ET

# Define the path of the XML file
xml_file = "C:\\Test\\employee1.xml"

# Parse the XML file and get the root element
tree = ET.parse(xml_file)
root = tree.getroot()

# Define a function to get job information from an element
def get_job_info(element):
    # Create an empty dictionary to store job information
    job_info = {}
    # Loop through the attributes of the element
    for key, value in element.attrib.items():
        # Add the attribute name and value to the dictionary
        job_info[key] = value
    # Loop through the child elements of the element
    for child in element:
        # Add the child tag and text to the dictionary
        job_info[child.tag] = child.text
    # Return the dictionary
    return job_info

# Get the first child element of the root element, which is <Job>
job_element = root[0]

# Get the job information from the job element
job_info = get_job_info(job_element)

# Print the job information
print(job_info)
