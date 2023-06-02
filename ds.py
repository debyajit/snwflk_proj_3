
awk -F "~" '{ if (NF < 68) { getline nextLine; $0 = $0 nextLine; } print }' input.csv > output.csv

awk '!/^2023/ { printf "%s", prev; prev = $0; next } { print prev; prev = $0 } END { print prev }' input.txt > output.txt


