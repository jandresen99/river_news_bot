import sys
import web_scrapper
import send_message

def update_news(token, chat_id):
    news = web_scrapper.get_newsV1()
    for item in news:
        message = item + "\n\n" + news[item]
        send_message.send_simple_message_to_group(message, chat_id, token)

if __name__ == '__main__':
    update_news(sys.argv[1], sys.argv[2])