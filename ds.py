
import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Open reference file
with open('reference.txt') as f:
    ref = f.readlines()

# Create output file
with open('output.txt', 'w') as f:
    # Write header
    f.write('PARENT_FOLDER,JOBNAME,VARIABLE name,VARIABLE value,REFERENCE FIELD 3,REFERENCE FIELD 4\n')

    # Loop through jobs
    for job in root.iter('JOB'):
        # Get job details
        parent_folder = job.attrib['PARENT_FOLDER']
        jobname = job.attrib['JOBNAME']

        # Loop through variables
        for var in job.iter('VARIABLE'):
            var_name = var.attrib['NAME']
            var_value = var.attrib['VALUE']

            # Find matching reference field
            for line in ref:
                if var_name in line:
                    ref_fields = line.strip().split('~')
                    ref_field_3 = ref_fields[2]
                    ref_field_4 = ref_fields[3]

                    # Write output row
                    f.write(f'{parent_folder},{jobname},{var_name},{var_value},{ref_field_3},{ref_field_4}\n')
