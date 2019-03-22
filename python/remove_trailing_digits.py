>>> mystring='bdm-issues-1234'
>>> mystring.rstrip()
'bdm-issues-1234'
>>> mystring.rstrip(string.digits)
'bdm-issues-'
>>> mystring.rstrip(string.digits).rstrip('-')
'bdm-issues'
>>> 
