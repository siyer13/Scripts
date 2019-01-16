# Regex to remove new lines between quotes, and not end of line
\n(?=(^[^\“]*\“[^\“]*\“)*[^\“]*$)


# gawk program for the same above
gawk -v RS='"' 'NR % 2 == 0 { gsub(/\n/, "") } { printf("%s%s", $0, RT) }' filewithquotes > filewithoutquotes

#sed to remove comma in between quote
sed -e ':a;N;$!ba;s/\n(?=(^[^\"]*\"[^\"]*\")*[^\"]*$)//g'
