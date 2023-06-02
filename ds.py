awk 'BEGIN{ RS=""; FS="\n"; OFS=""; ORS="\n" } { for (i=1; i<=NF; i++) { if ($i != "") { printf("%s~", $i) } } print "" }' input.txt > output.txt
