import xml.etree.ElementTree as ET

# Parse input XML file
tree = ET.parse('input_ctm.xml')
root = tree.getroot()

# Open reference file and store values in a dictionary
reference = {}
with open('reference.txt') as f:
    for line in f:
        fields = line.strip().split('~')
        reference[fields[1]] = (fields[2], fields[3])

# Print header
print('PARENT_FOLDER,JOBNAME,VARIABLE name,VARIABLE value,REFERENCE FIELD 3,REFERENCE FIELD 4')

# Process each JOB element
for job in root.iter('JOB'):
    # Get PARENT_FOLDER and JOBNAME attributes
    parent_folder = job.attrib['PARENT_FOLDER']
    jobname = job.attrib['JOBNAME']
    
    # Process each VARIABLE element
    for var in job.iter('VARIABLE'):
        # Get VARIABLE name and value attributes
        var_name = var.attrib['NAME']
        var_value = var.attrib['VALUE']
        
        # Look up var_value in reference dictionary
        if var_value in reference:
            ref_fields = reference[var_value]
        else:
            ref_fields = ('nomatch', '')
        
        # Print output
        print(f'{parent_folder},{jobname},{var_name},{var_value},{ref_fields[0]},{ref_fields[1]}')
