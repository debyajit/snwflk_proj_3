import xml.etree.ElementTree as ET

# Path to the sample DataStage job XML file
xml_file_path = "path/to/sample/job.dsx"

# Parse the XML file using ElementTree
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Print basic information from the JobHeader section
job_name = root.find("JobHeader/JobName")
if job_name is not None:
    print("Job Name: ", job_name.text)
else:
    print("Job Name not found")

job_description = root.find("JobHeader/JobDescription")
if job_description is not None:
    print("Job Description: ", job_description.text)
else:
    print("Job Description not found")

job_version = root.find("JobHeader/Version")
if job_version is not None:
    print("Job Version: ", job_version.text)
else:
    print("Job Version not found")

job_creator = root.find("JobHeader/Creator")
if job_creator is not None:
    print("Job Creator: ", job_creator.text)
else:
    print("Job Creator not found")

# Print the name and configuration of each stage in the JobDef section
for stage in root.findall("JobDef/Stage"):
    stage_name = stage.find("Name")
    if stage_name is not None:
        print("Stage Name: ", stage_name.text)
    else:
        print("Stage Name not found")

    stage_type = stage.get("stageType")
    if stage_type is not None:
        print("Stage Type: ", stage_type)
    else:
        print("Stage Type not found")

    for param in stage.findall("Properties/Property"):
        param_name = param.get("name")
        param_value = param.text
        if param_name is not None and param_value is not None:
            print("  ", param_name, ":", param_value)
        else:
            print("Parameter not found")

# Print any parameters defined in the JobParameters section
for param in root.findall("JobParameters/Parameter"):
    param_name = param.get("name")
    param_value = param.text
    if param_name is not None and param_value is not None:
        print("Parameter Name: ", param_name)
        print("Parameter Value: ", param_value)
    else:
        print("Parameter not found")

# Print any additional properties defined in the JobProperties section
for prop in root.findall("JobProperties/Property"):
    prop_name = prop.get("name")
    prop_value = prop.text
    if prop_name is not None and prop_value is not None:
        print("Property Name: ", prop_name)
        print("Property Value: ", prop_value)
    else:
        print("Property not found")
