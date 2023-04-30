
# Import the xml and csv modules
import xml.etree.ElementTree as ET
import csv

# Define the xml input file name
xml_input_file = "input.xml"

# Define the text input file name
text_input_file = "input.txt"

# Define the output file name
output_file = "ctm_out"

# Create a list to store the output data
output_data = []

# Parse the xml data
tree = ET.parse(xml_input_file)
root = tree.getroot()

# Loop through all the jobs in the folder
for job in root.find("FOLDER").findall("JOB"):
    # Get the application, sub_application, parent_folder and jobname attributes
    application = job.get("APPLICATION")
    sub_application = job.get("SUB_APPLICATION")
    parent_folder = job.get("PARENT_FOLDER")
    jobname = job.get("JOBNAME")
    # Loop through all the variables in the job
    for variable in job.findall("VARIABLE"):
        # Get the variable name and value attributes
        variable_name = variable.get("NAME")
        variable_value = variable.get("VALUE")
        # Check if the variable name starts with PARM
        if variable_name.startswith("PARM"):
            # Create a dictionary to store the information
            output_dict = {}
            output_dict["APPLICATION"] = application
            output_dict["SUB_APPLICATION"] = sub_application
            output_dict["PARENT_FOLDER"] = parent_folder
            output_dict["JOBNAME"] = jobname
            output_dict["VARIABLE_NAME"] = variable_name
            output_dict["VARIABLE_VALUE"] = variable_value
            # Append the dictionary to the output data list
            output_data.append(output_dict)

# Read the text data into a dictionary
text_data = {}
with open(text_input_file) as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        # Use the second field as the key and the third and fourth fields as the value
        text_data[row[1]] = (row[2], row[3])

# Loop through the output data list
for output_dict in output_data:
    # Get the variable value from the dictionary
    variable_value = output_dict["VARIABLE_VALUE"]
    # Check if the variable value matches any key in the text data
    if variable_value in text_data:
        # Get the third and fourth fields from the text data
        field3, field4 = text_data[variable_value]
    else:
        # Set the third and fourth fields to empty strings
        field3, field4 = "", ""
    # Add the third and fourth fields to the dictionary
    output_dict["FIELD3"] = field3
    output_dict["FIELD4"] = field4

# Open the output file for writing
with open(output_file, "w") as f:
    # Create a csv writer object
    writer = csv.DictWriter(f, fieldnames=["APPLICATION","SUB_APPLICATION","PARENT_FOLDER","JOBNAME","VARIABLE_NAME","VARIABLE_VALUE","FIELD3","FIELD4"])
    # Write the header line
    writer.writeheader()
    # Write all the dictionaries in the output data list
    writer.writerows(output_data)

# Print a message to indicate success
print(f"Results saved to {output_file}")
```
