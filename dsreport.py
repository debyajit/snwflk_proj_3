import xmltodict

with open("input.xml") as f:
  xml_data = f.read()
  dict_data = xmltodict.parse(xml_data)
  # dict_data is a dictionary that contains the XML data

with open("reference.txt") as f:
  ref_data = f.read()
  ref_list = ref_data.split("~")
  # ref_list is a list that contains the fields from the reference file

OP1 = {} # initialize an empty dictionary
for job in dict_data["DEFTABLE"]["FOLDER"]["JOB"]: # loop over each job in the input file
  jobname = job["@JOBNAME"] # get the job name
  parent_folder = job["@PARENT_FOLDER"] # get the parent folder
  OP1[jobname] = {} # initialize a sub-dictionary for each job name
  OP1[jobname]["PARENT_FOLDER"] = parent_folder # store the parent folder
  for var in job["VARIABLE"]: # loop over each variable in the job
    var_name = var["@NAME"] # get the variable name
    var_value = var["@VALUE"] # get the variable value
    OP1[jobname][var_name] = var_value # store the variable name and value
    if var_value == ref_list[1]: # check if the variable value matches the second field from the reference file
      OP1[jobname]["REF_FIELD_3"] = ref_list[2] # add the third field from the reference file
      OP1[jobname]["REF_FIELD_4"] = ref_list[3] # add the fourth field from the reference file
    else:
      OP1[jobname]["REF_FIELD_3"] = "no match" # if no match, populate with "no match"
      OP1[jobname]["REF_FIELD_4"] = "no match" # if no match, populate with "no match"

        for jobname in OP1: # loop over each job name in OP1
  if "." in ref_list[1]: # check if there is a "." character in the second field from the reference file
    OP1[jobname]["DERIVED_FIELD"] = "A" # populate with "A"

    with open("output.txt", "w") as f: # open an output text file for writing
  for jobname in OP1: # loop over each job name in OP1
    parent_folder = OP1[jobname]["PARENT_FOLDER"] # get the parent folder
    f.write(parent_folder + ",") # write it to the output file with a comma
    f.write(jobname + ",") # write the job name to the output file with a comma
    for var_name in OP1[jobname]: # loop over each variable name in OP1[jobname]
      if var_name not in ["PARENT_FOLDER", "REF_FIELD_3", "REF_FIELD_4", "DERIVED_FIELD"]: # exclude these fields as they are already written or will be written later
        var_value = OP1[jobname][var_name] # get the variable value
        f.write(var_name + "," + var_value + ",") # write them to the output file with commas
    ref_field_3 = OP1[jobname]["REF_FIELD_3"] # get the third field from the reference file
    f.write(ref_field_3 + ",") # write it to the output file with a comma
    ref_field_4 = OP1[jobname]["REF_FIELD_4"] # get the fourth field from the reference file
    f.write(ref_field_4 + ",") # write it to the output file with a comma
    derived_field = OP1[jobname]["DERIVED_FIELD"] # get the derived field 
    f.write(derived_field + "\n") # write it to the output file with a newline character
