import xml.etree.ElementTree as ET

def main():
    # Get the input XML file name
    xml_file_name = input("Enter the input XML file name: ")

    # Read the XML file
    tree = ET.parse(xml_file_name)

    # Get the root of the XML tree
    root = tree.getroot()

    # Create a YAML file
    yml_file = open("output.yml", "w")

    # Write the job details to the YAML file
    yml_file.write("job:\n")
    yml_file.write("  name: " + root.attrib["Name"] + "\n")
    yml_file.write("  desc: " + root.attrib["Desc"] + "\n")
    yml_file.write("  status: " + root.attrib["Status"] + "\n")
    yml_file.write("  waveNo: " + root.attrib["WaveNo"] + "\n")
    yml_file.write("  startDateTime: " + root.attrib["StartDateTime"] + "\n")
    yml_file.write("  endDateTime: " + root.attrib["EndDateTime"] + "\n")
    yml_file.write("  elapsedTime: " + root.attrib["ElapsedTime"] + "\n")
    yml_file.write("  elapsedSecs: " + root.attrib["ElapsedSecs"] + "\n")

    # Write the ParamSet details to the YAML file
    yml_file.write("paramSet:\n")
    for param in root.findall("ParamSet/Param"):
        yml_file.write("  name: " + param.attrib["Name"] + "\n")
        yml_file.write("  type: " + param.attrib["Type"] + "\n")
        yml_file.write("  desc: " + param.attrib["Desc"] + "\n")
        yml_file.write("  value: " + param.attrib["Value"] + "\n")

    # Write the Stage details to the YAML file
    yml_file.write("stages:\n")
    for stage in root.findall("ComponentSet/Stage"):
        yml_file.write("  name: " + stage.attrib["Name"] + "\n")
        yml_file.write("  stageStatus: " + stage.attrib["StageStatus"] + "\n")
        yml_file.write("  stageType: " + stage.attrib["StageType"] + "\n")
        yml_file.write("  desc: " + stage.attrib["Desc"] + "\n")
        yml_file.write("  startDateTime: " + stage.attrib["StartDateTime"] + "\n")
        yml_file.write("  endDateTime: " + stage.attrib["EndDateTime"] + "\n")
        yml_file.write("  elapsedTime: " + stage.attrib["ElapsedTime"] + "\n")
        yml_file.write("  elapsedSecs: " + stage.attrib["ElapsedSecs"] + "\n")

        # Write the InputLinks details to the YAML file
        yml_file.write("  inputLinks:\n")
        for input_link in stage.findall("InputLinks/Link"):
            yml_file.write("    name: " + input_link.attrib["Name"] + "\n")
            yml_file.write("    linkType: " + input_link.attrib["LinkType"] + "\n")
            yml_file.write("    desc: " + input_link.attrib["Desc"] + "\n")
            yml_file.write("    stage: " + input_link.attrib["Stage"] + "\n")

        # Write the OutputLinks details to the YAML file
        yml_file.write("  outputLinks:\n")
        for output_link in stage.findall("OutputLinks/Link"):
            yml_file.write("    name: " + output_link.attrib["Name"] + "\n")
            yml_file.write("    linkType: " + output_link.attrib["LinkType"] + "\n")
            yml
