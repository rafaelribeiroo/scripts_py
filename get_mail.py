from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from libtorrent import session, parse_magnet_uri
from bs4 import BeautifulSoup as beauty
from email import message_from_bytes
from traceback import print_exc
from selenium import webdriver
from imaplib import IMAP4_SSL
from re import compile, S, M
from psycopg2 import connect
from time import sleep, time
from decouple import config
from datetime import date

today = date.today()

connection = connect(
    host='localhost',
    database='rarbg',
    user='postgres',
    password=config('PASSWORD_DB')
)
cursor = connection.cursor()

FROM_EMAIL = config('FROM_MAIL')
FROM_PWD = config('PASSWORD')
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

session = session(
    {'listen_interfaces': '0.0.0.0:6881,6882,6883,6884,6885,6886,6887,6888'}
)


def read_mail_from_gmail():
    try:
        mail = IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        filter_mail = mail.search(
            None,
            'SUBJECT',
            f'"Movies Added in RARbg ({today.strftime("%d/%m/%Y")})"'
        )
        if not filter_mail[1][0].decode():
            print('There\'s none mails matching your search')
            quit()

        # 0 gets first // -1 gets last mail received
        data = mail.fetch(str(int(filter_mail[1][0].split()[-1])), '(RFC822)')

        # from pdb import set_trace; set_trace()
        bytes_data = data[1][0][1]
        msg = message_from_bytes(bytes_data)
        # msg["subject || to || from"]
        for part in msg.walk():
            if part.get_content_type() in ['text/plain', 'text/html']:
                content = part.get_payload(decode=True)
                # import pdb; pdb.set_trace()
                global request
                request = content.decode()

    except Exception as e:
        print_exc()
        print(str(e))


read_mail_from_gmail()

remove_content_from_tags = compile(r'<div.*?><div.*?>(.*?)</div>', S | M)
match = remove_content_from_tags.match(request)
request = match.groups()[0].strip()
list_requests = list(request.split(' '))

if list_requests:
    for torrent in list_requests:
        cursor.execute(f"SELECT url FROM torrent WHERE id = '{torrent}'")
        url = cursor.fetchone()[0]
        if url:
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            driver = webdriver.Chrome(
                options=chrome_options,
                service=Service(ChromeDriverManager().install())
            )

            driver.get(f'https://rarbgproxied.org{url}')
            html = driver.page_source
            soup = beauty(html, 'html.parser')
            magnet = soup.select("a[href*=magnet]")[0]['href']
            driver.close()

            params = parse_magnet_uri(magnet)
            params.save_path = '/home/ribeiroo/Downloads/'
            # ses.add_torrent_async(params)
            handle = session.add_torrent(params)
            # handle.set_download_limit(2048)

            begin = time()

            while not handle.status().has_metadata:
                sleep(1)
            print('Downloaded Metadata.')
            print("\nStarting", handle.status().name)

            while not handle.status().is_seeding:
                s = handle.status()

                # state_str = ['Queued', 'Checking', 'Downloading Metadata',
                # 'Downloading', 'Finished', 'Seeding', 'Allocating',
                # 'Checking Fastresume']

                # %s: state_str[s.state]
                print(
                    f'{s.progress * 100:.2f}% complete'
                    f' | Down: {s.download_rate / 1000000:.1f} mb/s'
                    f' | Up: {s.upload_rate / 1000000:.1f} mb/s'
                    f' | Peers: {s.num_peers}',
                    flush=True
                )
                sleep(5)

            end = time()

            print(handle.status().name, "Complete")
            print('Elasped Time:', int((end - begin) // 60), 'min\n')

cursor.close()
connection.close()

print('Done!')
