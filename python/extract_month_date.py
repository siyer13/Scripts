# program to extract month date and year from a given date
from datetime import datetime,date
def extractor(given_date):
    date_map = {}
    format_string = '%m-%d-%Y'
    extract = datetime.strptime(given_date,format_string)
    date_map.update({'day':extract.day, 'month' : extract.month})
    return date_map
