#!/Users/siyer/virtualenv/flask/bin/python
from sqlalchemy import create_engine


file_path = '/Users/siyer/Documents/MF_DATA/12-Mar-2017-NAV1.txt'
#for line in open(file_path,'r'):
#    print line

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta

def insert_data(fund_type,fund_name,fund_value):
    db_string = 'postgres://siyer@localhost:5432/siyer'
    db = create_engine(db_string)
    #db.execute("Insert into nav (fund_type,fund_name) values ("+ str(fund_type) +","+ str(fund_name) + ")")

    db.execute("Insert into nav (scheme_code,isin_div_payout__isin_growth,isin_div_reinvestment,scheme_name,net_asset_value,repurchase_price,sale_price,date,fund_type,fund_name) values ('" + fund_value[0] + "','" +  fund_value[1] + "','" +fund_value[2] + "','" +fund_value[3].replace("'","") + "','" +fund_value[4] + "','" +fund_value[5] + "','" +fund_value[6] + "','" +fund_value[7] + "','" + fund_type + "','" + fund_name + "')")


def parse_funds(fund_value):
    nav = fund_value.split(';')
    new_list = []
    counter = 1
    if len(nav) == 8:
        new_list = nav
    else:
        for values in nav:
            #print values
            if counter == 8 or counter == 7:
                #print counter
                if ' 'in values:
                    temp = values
                    val = values.split(' ')
                    new_list.append(val[0])
                    new_list.append(val[1])
                    counter = 1
                else:
                    new_list.append(values)
                    counter = counter + 1
            else:
                new_list.append(values)
                counter = counter + 1


    return new_list

with open(file_path) as file:
    file_list = file.readlines()[2:]
# remove first two lines (headers and space)
file_list = file_list[0::2]
counter = 1
fund_type = ''
fund_name = ''
fund_value= ''
for data in file_list:
    if counter == 2:
        if ';' in data:
            fund_value = data.strip()
            fund_value = parse_funds(fund_value)
            #if len(fund_value) % 8 != 0:
            #    print 'oyee'
            # if len(fund_value) == 29:
            #     print fund_type
            #     print fund_name
            #     #print len(fund_value)
            #     print fund_value
            #print len(fund_value)
            #print fund_value
            print fund_type
            print fund_name
            print fund_value
            insert_data(fund_type,fund_name,fund_value)

            counter = 1
        else:
            fund_type = fund_name
            fund_name = data.strip()
    else:
        fund_name = data.strip()
        counter = counter + 1
