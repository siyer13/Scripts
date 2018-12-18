from extract_month_date import extractor

zodiac_sign = [
'ARIES',
'TAURUS',
'GEMINNI',
'CANCER',
'LEO',
'VIRGO',
'LIBRA',
'SCORPIO',
'SAGGITARRIUS',
'CAPRICORN',
'AQUARIUS',
'PIESCES'
]


#print(zodiac_sign[0])

def get_zodiac_sign(dob):
    dob_map = extractor(dob)
    sign = ''
    day = dob_map.get('day')
    month = dob_map.get('month')
    if (int(day) >= 21 and int(month) == 3)  or (int(day) <= 19 and int(month) == 4):
        sign = zodiac_sign[0]
    return sign

print(get_zodiac_sign('04-04-1994'))
print(get_zodiac_sign('13-06-1984'))
