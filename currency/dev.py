def curr(money, currency):
    if currency == 'usd':
        return f'{round(money * 0.39, 2)} USD'
    if currency == 'eur':
        return f'{round(money * 0.361, 2)} EUR'
    if currency == 'rub':
        return f'{round(money * 39, 2)}RUB'
    else:
        return "error"