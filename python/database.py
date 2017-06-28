import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey

def connect(db, user='postgres', password='Rambo@1984', host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


con,meta = connect('tennis')
slams = Table('slams',meta,
        Column('name', String, primary_key=True),
        Column('country',String))

results = Table('results',meta,
        Column('slam',String, ForeignKey('slams.name')),
        Column('year',Integer),
        Column('result',String))

# create the above tables
meta.create_all(con)

clause = slams.insert().values(name='Wimbledon', country='United Kingdom')

con.execute(clause)

# Insert list of values into results table
victories = [
    {'slam': 'Wimbledon', 'year': 2003, 'result': 'W'},
    {'slam': 'Wimbledon', 'year': 2004, 'result': 'W'},
    {'slam': 'Wimbledon', 'year': 2005, 'result': 'W'}
]

con.execute(meta.tables['results'].insert(), victories)
