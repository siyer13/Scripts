from urllib.request import urlopen
import datetime

now = datetime.datetime.now()
file_name = now.strftime('%d'),'-',now.strftime('%b'),'-',now.strftime('%Y'),'.txt'
file_name = ''.join(file_name)
print(file_name)


data = urlopen('https://www.amfiindia.com/spages/NAVAll.txt').read()

mutual_fund_nav_file = open(file_name,"wb")

mutual_fund_nav_file.write(data)

mutual_fund_nav_file.close()
