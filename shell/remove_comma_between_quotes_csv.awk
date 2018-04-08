siyer@vedam:~/Work/tmp$ awk -F'"' -v OFS='' '{ for (i=2; i<=NF; i+=2) gsub(",", "", $i) } 1' team_contacts.csv > team_contacts_1.csvimport csv
