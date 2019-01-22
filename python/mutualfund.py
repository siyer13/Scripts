import csv
import pymysql.cursors
import os

fund_name =''
scheme_type = ''
scheme_name = ''
scheme_code = ''
isin_div_payout = ''
isin_div_reinvestment = ''
net_asset_value = ''
fund_value_date = ''
load_date=''

fund_file = 'C:\\Users\\Sridhar\\Documents\\GitHub\\Scripts\\python\\data\\21-Jan-2019.txt'

connection = pymysql.connect(host='localhost',user='root',password='Rambo@1984',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
connection.select_db('mutual_fund')

with open(fund_file,'r') as mf_file:
    load_date =  os.path.splitext(os.path.basename(fund_file))[0]
    print(load_date)
    csv_reader = csv.reader(mf_file,delimiter=';')
    line_count = 0
    next(csv_reader, None)
    for row in csv_reader:
        #print(row)
        if len(row) == 1 and ('(') in row[0]:
            scheme_type = row[0]
            #print('scheme_type: ', scheme_type)
        elif len(row) == 1 and row[0] != ' ':
            fund_name = row[0]
            #print('scheme_name: ', scheme_name)
        elif len(row) == 0:
            continue
        elif row[0] != ' ' :
            scheme_code = row[0]
            isin_div_payout = row[1]
            isin_div_reinvestment = row[2]
            scheme_name = row[3].replace("'", "")
            #print(scheme_name)
            net_asset_value = row[4]
            if net_asset_value == 'N.A.':
                net_asset_value = 0.0
            fund_value_date = row[5]
            query = """INSERT INTO mutual_fund.scheme(fund_name,scheme_type,scheme_code,scheme_name,isin_div_payout,isin_div_reinvestment,net_asset_value,fund_value_date,load_date) VALUES ('{fund_name}','{scheme_type}','{scheme_code}','{scheme_name}','{isin_div_payout}','{isin_div_reinvestment}',{net_asset_value},'{fund_value_date}','{load_date}') """.format(fund_name=fund_name,scheme_type=scheme_type,scheme_code=scheme_code,scheme_name=scheme_name,isin_div_payout=isin_div_payout,isin_div_reinvestment=isin_div_reinvestment,net_asset_value=net_asset_value,fund_value_date=fund_value_date,load_date=load_date)
            print(query)
            cursor.execute(query)
            connection.commit()
mf_file.close()
connection.close()
