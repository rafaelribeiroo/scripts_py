from flask import Response, request
from decouple import config
from random import randint
from requests import post
from flask import Flask

quotes = (
    'Ilyena, my love, forgive me!',
    'A man who trusts everyone is a fool, and a man who trusts no one is a '
    'fool. We are all fools, if we live long enough.',
    'What you want is what you cannot have. What you cannot have is what '
    'you want.',
    'The Wheel of Time and the wheel of a man\'s life turn alike without '
    'pity or mercy.',
    'What makes you think you can keep anyone safe? We are all going to die. '
    'Just hope that you aren\'t the one who kills them.',
    'Mustn\'t use that. Threatens the fabric of the pattern. Not even for '
    'Ilyena? I would burn the world and use my soul for tinder to hear her'
    ' laugh again.',
    'Break it break them all must break them must must must break them all '
    'break them and strike must strike quickly must strike now break it '
    'break it break it...',
    'He\'s insane and I\'m not. Besides, he failed and I won\'t',
    'Kill him, kill him now!'
)

TOKEN = config('BOT_TOKEN')
app = Flask(__name__)


def parse_message(message):
    print("message-->", message)
    # import pdb; pdb.set_trace()
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("got text message :", txt)
    print("chat_id-->", chat_id)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{config("BOT_TOKEN")}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }

    r = post(url, json=payload)
    return r

# import pdb; pdb.set_trace()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)
        if 'rand' in txt.lower():
            tel_send_message(chat_id, f'<i>{quotes[randint(0, len(quotes)-1)]}</i>')

        return Response('ok', status=200)
    else:
        return "<h1>Boas-vindas!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
