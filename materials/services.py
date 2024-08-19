import requests


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        'http://api.currencyapi.com/v3/latest?apikey=cur_live_EIAV8SvKqqFNjLgdSh0OHdtMcMDONzT45RhllViZ&currencies=RUB'
    )
    if response.status_code == 200:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate
    return usd_price
