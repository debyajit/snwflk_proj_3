import os

dc_1 = {
    'ABC': {
        'PARENT_FOLDER': 'FLD',
        'ref_1': 'DS',
        'ref_2': 'dsjb1'
    },
    'DEF': {
        'PARENT_FOLDER': 'FLD',
        'ref_1': 'FP',
        'ref_2': ''
    }
}

for key, value in dc_1.items():
    ref_2 = value['ref_2']
    if ref_2.startswith('ds'):
        command = f"dsjob {ref_2}"
        output_file = f"output_{key}.txt"

        # Change directory to /Scripts
        os.chdir("/Scripts")

        # Run the command and capture the output in a file
        os.system(f"{command} > {output_file}")

        # Write dc_1 row to the output file
        with open(output_file, 'a') as f:
            f.write(f"\ndc_1 row: {key}: {value}")

        # Change back to the previous directory
        os.chdir("..")
