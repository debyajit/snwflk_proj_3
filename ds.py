#!/bin/bash

input_file="$1"
output_file="output.csv"

# Delete blank lines from input file
sed '/^$/d' "$input_file" > "$output_file"

# Concatenate lines that don't start with "2023" with previous line
awk -F "~" 'BEGIN {OFS="~"; prev=""} { if ($1 ~ /^2023/) { if (prev != "") print prev; prev=$0; } else { prev = prev $0 } } END { print prev }' "$output_file" > "$output_file.tmp"

# Append any remaining concatenated line to the output file
cat "$output_file.tmp" >> "$output_file"

# Remove temporary file
rm "$output_file.tmp"
