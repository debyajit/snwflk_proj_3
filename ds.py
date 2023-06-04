#!/bin/bash

# Check if the file name is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide the file name as an argument."
  exit 1
fi

# Store the file name from the argument
file="$1"

# Create a new file name for the output
output_file="${file}_output"

# Read the file line by line and find the line number with a blank line
blank_line_num=0
while IFS='' read -r line || [[ -n "$line" ]]; do
  ((blank_line_num++))
  if [[ -z $line ]]; then
    break
  fi
done < "$file"

# Delete the line with line number = blank_line_num
sed -i "${blank_line_num}d" "$file"

# Concatenate the lines with line numbers blank_line_num-1 and blank_line_num
if [ "$blank_line_num" -gt 1 ]; then
  awk -v line_num=$((blank_line_num-1)) 'NR==line_num{line=$0} NR==line_num+1{$0=$0 line} NR!=line_num{print}' "$file" > "$output_file"
else
  cp "$file" "$output_file"
fi

# Print the success message
echo "Output written to $output_file"
