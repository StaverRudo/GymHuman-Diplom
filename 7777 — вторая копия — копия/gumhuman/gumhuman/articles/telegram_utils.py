import requests
import json

def send_telegram_message(chat_id, message):
    token = '6220742531:AAHpR85aEWuKTIVGpzVoJ6B4nAP0yqQ0C0I'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    headers = {'Content-Type': 'application/json'}
    payload = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()
