def currency_amt(currency, amount) :
    if currency == 'USD' and (amount == None or amount == ''):
        return 10
    elif currency == 'USD' and amount != None:
        return amount
    elif currency == None and amount == None:
        return 0
    else:
        return 100


print(currency_amt('USD',''))
