import xml.etree.ElementTree as ET
import csv

# Read the input XML file
xml_file = open("input.xml", "r")
xml_tree = ET.parse(xml_file)

# Read the reference text file
reference_file = open("reference.txt", "r")
reference_reader = csv.reader(reference_file, delimiter="~")

# Create a dictionary to store the output data
op1 = {}

# Iterate over the XML tree
for job in xml_tree.findall(".//JOB"):

    # Get the parent folder, job name, and variable name
    parent_folder = job.get("PARENT_FOLDER")
    job_name = job.get("JOBNAME")

    # Check if the variable element exists
    if job.find("VARIABLE") is not None:
        variable_name = job.find("VARIABLE").get("NAME")
    else:
        variable_name = None

    # Get the corresponding data from the reference file
    for row in reference_reader:
        if variable_name is not None and row[0] == variable_name:
            if row:
                op1[job_name] = {
                    "PARENT_FOLDER": parent_folder,
                    "JOBNAME": job_name,
                    "VARIABLE_NAME": variable_name,
                    "VARIABLE_VALUE": row[1],
                    "REFERENCE_1": row[2],
                    "REFERENCE_2": row[3],
                }
                break

    # Check if the variable was found in the reference file
    if variable_name is not None and variable_name not in op1:
        op1[job_name] = {
            "PARENT_FOLDER": parent_folder,
            "JOBNAME": job_name,
            "VARIABLE_NAME": variable_name,
            "VARIABLE_VALUE": row[1],
            "REFERENCE_1": "no match",
            "REFERENCE_2": "no match",
        }

    # Check if the reference file has a . character in the second field
    if "." in op1.get(job_name, {}).get("REFERENCE_1", ""):
        op1[job_name]["HAS_DOT"] = "A"
    else:
        op1[job_name]["HAS_DOT"] = "B"

# Iterate over the output dictionary
for job in op1:

    # Go to the /proj/scripts directory
    os.chdir("/proj/scripts")

    # Execute the dsreport command
    dsreport_command = "dsreport " + op1[job]["REFERENCE_2"]
    dsreport_output = subprocess.check_output(dsreport_command, shell=True)

    # Save the dsreport output to a file
    with open("dsreport_output.xml", "wb") as f:
        f.write(dsreport_output)

