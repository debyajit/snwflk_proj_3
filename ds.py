awk 'BEGIN{ RS=""; FS="\n"; OFS=""; ORS="\n" } { for (i=1; i<=NF; i++) { if ($i != "") { printf("%s~", $i) } } print "" }' input.txt > output.txt

awk 'BEGIN{ RS="\n\n"; FS="\n"; ORS="" } { for (i=1; i<=NF; i++) { if (i == 1) printf("%s", $i); else printf("~%s", $i); } print "" }' input.txt > output.txt

awk -F "~" '{ if (NF < 68) { getline nextLine; $0 = $0 nextLine; } print }' input.csv > output.csv

