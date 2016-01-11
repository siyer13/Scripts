FNR == NR {
  File_1[$29] = $29
next
}

{ if (!($29 in File_1)) print $0; }
