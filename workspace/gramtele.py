from requests import get, post
from decouple import config
from random import randint

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

token = config('BOT_TOKEN')


def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    res = get(url=url)
    update = res.json()["result"]
    return update


def last():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    res = get(url=url)
    import pdb; pdb.set_trace()
    update = res.json()["result"]
    return update[-1]


def parse_message():
    chat_id = last()['message']['chat']['id']
    txt = last()['message']['text']
    txt_id = last()['message']['message_id']
    return chat_id, txt, txt_id


# def randomPhoto():
#     url = f'https://dog.ceo/api/breeds/image/random'
#     res = get(url)
#     img_url = res.json()["message"]
#     return img_url


def reply_markup(ids):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': ids,
        'text': quotes[randint(0, len(quotes) - 1)],
        'reply_to_message_id': txt_id,
        'parse_mode': 'HTML'
    }

    r = post(url, json=payload)
    return r.json()


# def sendPhoto(ids):
#     url = f'https://api.telegram.org/bot{token}/sendPhoto'
#     photo = randomPhoto()
#     p = {
#         "chat_id": ids,
#         "photo": photo,
#     }
#     res = get(url, params=p)
#     return res.json()


len_update = len(getUpdates())
last_len_update = len(getUpdates())

while True:
    last_len_update = len(getUpdates())
    chat_id, txt, txt_id = parse_message()

    import pdb; pdb.set_trace()

    if last_len_update == len_update:
        if txt == '/start':
            print('i\'m here')
            len_update = last_len_update
        elif 'rand' in txt.lower():
            reply_markup(chat_id, txt_id)
            len_update = last_len_update
