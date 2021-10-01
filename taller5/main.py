import json
import requests
import pywhatkit
import datetime
import schedule
import time
from urllib.parse import quote
import pyautogui as pt
import webbrowser as web

number = '''
    +50240293770
'''

def job():
    now = datetime.datetime.now()

    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    a = json.loads(r.text)
    btc_string = "1 BITCOIN te costará " + str(a["bitcoin"]["usd"]) + " USD"
    
    pywhatkit.sendwhatmsg_instantly(number, "Hola!, " + btc_string,  wait_time=15)
    
job()
schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)