#!/bin/bash

# Check if file name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <file_name>"
  exit 1
fi

# Remove blank lines
sed '/^$/d' "$1" > temp.csv

# Concatenate lines that do not start with "2023"
awk -F"~" 'NR==1 {print $0} NR>1 {if ($1 ~ /^2023/) {if (line) print line; line=$0} else {line=line"~"$0}} END {print line}' temp.csv > output.csv

# Remove temporary file
rm temp.csv

echo "Output written to output.csv"

#############################
#!/bin/bash

# Check if file name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <file_name>"
  exit 1
fi

input_file="$1"
output_file="${input_file%.*}.txt"

# Remove blank lines
sed '/^$/d' "$input_file" > temp.csv

# Concatenate lines that do not start with "2023"
awk -F"~" 'NR==1 {print $0} NR>1 {if ($1 ~ /^2023/) {if (line) print line; line=$0} else {line=line""$0}} END {print line}' temp.csv > "$output_file"

# Remove temporary file
rm temp.csv

echo "Output written to $output_file"
