
awk -F "~" '{ if (NF < 68) { getline nextLine; $0 = $0 nextLine; } print }' input.csv > output.csv

awk '!/^2023/ { printf "%s", prev; prev = $0; next } { print prev; prev = $0 } END { print prev }' input.txt > output.txt


#!/bin/bash

# Input and output file paths
input_file="input.txt"
output_file="output.txt"

# Read the input file line by line
while IFS= read -r line; do
  # Check if the line starts with "2023"
  if [[ $line == 2023* ]]; then
    # Output the line as is
    echo "$line" >> "$output_file"
  else
    # Concatenate the line with the previous line
    concatenated_line=$(echo -e "${concatenated_line}${line}")
    # Check if the concatenated line contains 68 delimiters
    delimiter_count=$(awk -F "~" '{print NF-1}' <<< "$concatenated_line")
    if [[ $delimiter_count -eq 68 ]]; then
      # Output the concatenated line with the end of line character
      echo "${concatenated_line}$" >> "$output_file"
      # Reset the concatenated line
      concatenated_line=""
    fi
  fi
done < "$input_file"


