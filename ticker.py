#!/usr/bin/python3

import requests, json
from time import sleep
from lcdlib import LCD

DELAY = 5
CONSOLE_PRINT = False

def priceBTCUSD():
    r = requests.get('https://blockchain.info/ticker')
    data = json.loads(r.text)
    return data['USD']['15m']

def main():
    lcd = LCD()
    prev = 0
    while True:
        try:
            price = priceBTCUSD()
            if CONSOLE_PRINT: print(price)
            if price != prev:
                lcd.clear()
                lcd.message('{:^16}\n{:^16}'.format('USD$' + str(price), 'BTCUSD'))
                prev = price
            sleep(DELAY)
        except KeyboardInterrupt:
            lcd.clear()
            lcd.message('{:^16}'.format('Bot Offline'))
            break
        except Exception:
            pass

if __name__ == '__main__':
    main()
