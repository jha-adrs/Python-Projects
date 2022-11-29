import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time



try:
    while(True):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '2',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '{CoinmarketCap-API-Key}',
        }

        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        quote = (data.get('data'))[0].get('quote')
        USD = quote.get('USD')
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        quote = (data.get('data'))[1].get('quote')
        USD2 = quote.get('USD')
        btc = "$"+str(USD.get('price'))
        eth = "$"+str(USD2.get('price'))
        parameters = {"value1": btc, "value2": eth}
        # IFTTT API Key can be accessed by opening Documentation link in IFTTT website
        IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{event-name}/with/key/{Your-IFTTT-Key}'
        event = 'bitcoin_price_alert'
        ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
        requests.post(ifttt_event_url, json=parameters)
        print("Done")
        # Automates the requests to every 10 minutes
        time.sleep(600)


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)