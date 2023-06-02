
awk -F "~" '{ if (NF < 68) { getline nextLine; $0 = $0 nextLine; } print }' input.csv > output.csv


awk -F "~" '{
  if (NF < 68) {
    getline nextLine;
    if (NF + split(nextLine, fields, "~") < 68) {
      $0 = $0 nextLine;
    } else {
      print;
      $0 = nextLine;
    }
  }
  print
}' input.csv > output.csv

