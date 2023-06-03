
awk -F "~" '{ if (NF < 68) { getline nextLine; $0 = $0 nextLine; } print }' input.csv > output.csv

awk '!/^2023/ { printf "%s", prev; prev = $0; next } { print prev; prev = $0 } END { print prev }' input.txt > output.txt

#!/bin/bash

input_file="input.txt"
output_file="output.txt"
delimiter="~"
line_count=0
current_line=""
previous_line=""

while IFS= read -r line
do
    if [[ $line_count -eq 0 ]]; then
        previous_line=$line
    else
        if [[ $line =~ ^2023 ]]; then
            echo "$previous_line" >> "$output_file"
            previous_line=$line
        else
            previous_line+="$(printf "${delimiter}%s" "$line")"
        fi
    fi

    line_count=$((line_count + 1))
done < "$input_file"

# Add the last line to the output file
echo "$previous_line" >> "$output_file"



