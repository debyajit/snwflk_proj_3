import xml.etree.ElementTree as ET

# Path to the sample DataStage job XML file
xml_file_path = "path/to/sample/job.dsx"

# Parse the XML file using ElementTree
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Print basic information from the JobHeader section
print("Job Name: ", root.find("JobHeader/JobName").text)
print("Job Description: ", root.find("JobHeader/JobDescription").text)
print("Job Version: ", root.find("JobHeader/Version").text)
print("Job Creator: ", root.find("JobHeader/Creator").text)

# Print the name and configuration of each stage in the JobDef section
for stage in root.findall("JobDef/Stage"):
    print("Stage Name: ", stage.find("Name").text)
    print("Stage Type: ", stage.get("stageType"))
    for param in stage.findall("Properties/Property"):
        print("  ", param.get("name"), ":", param.text)

# Print any parameters defined in the JobParameters section
for param in root.findall("JobParameters/Parameter"):
    print("Parameter Name: ", param.get("name"))
    print("Parameter Value: ", param.text)

# Print any additional properties defined in the JobProperties section
for prop in root.findall("JobProperties/Property"):
    print("Property Name: ", prop.get("name"))
    print("Property Value: ", prop.text)
