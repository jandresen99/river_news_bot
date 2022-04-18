import requests

def send_simple_message_to_group(message, chat_id, token):
    send_message_url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id=-" + str(chat_id) + "&text=\"" + message + "\""
    response = requests.request("GET", send_message_url)
    print(response.status_code)