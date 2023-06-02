perl -ane '
  if (/^$/) {
    next;
  }
  
  if (defined $prev_line) {
    print "$prev_line~$_\n";
  } else {
    print $_;
  }

  $prev_line = $_;
' file.txt
