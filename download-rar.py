from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as beauty
from selenium import webdriver
from psycopg2 import connect
from decouple import config
from datetime import date
from smtplib import SMTP
from re import search

today = date.today()
# https://stackoverflow.com/questions/41918836/how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python

connection = connect(
    host='localhost',
    database='rarbg',
    user='postgres',
    password=config('PASSWORD_DB')
)

snd = config('FROM_MAIL')
rcv = config('TO_MAIL')
sbj = f'Movies Added in RARbg ({today.strftime("%d/%m/%Y")})'
passwd = config('PASSWORD')

# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(
    options=chrome_options,
    service=Service(ChromeDriverManager().install())
)
driver.get('https://rarbgproxied.org/torrents.php')

try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'lista')))
except TimeoutException:
    print("Loading took too much time!")

html = driver.page_source
soup = beauty(html, 'html.parser')

# import pdb; pdb.set_trace()

cursor = connection.cursor()
attachment = {}
for iterate in range(0, 8):
    title = soup.find_all("td", {
        "class": "lista",
        "align": "left",
        "valign": "top"
    })[iterate].a['title']

    url = soup.find_all("td", {
        "class": "lista",
        "align": "left",
        "valign": "top"
    })[iterate].a['href']

    clear_title = title[0:title.find(
        search('20[0-9][0-9]', title)[0]) - 1].replace('.', ' ')

    cursor.execute(
        'SELECT EXISTS ( SELECT 1 FROM torrent WHERE title = %s )',
        (f'{clear_title}',))

    if cursor.fetchone()[0] is False:
        cursor.execute("INSERT INTO torrent (title, url) VALUES "
                       f"('{clear_title}', '{url}') RETURNING id")
        data = cursor.fetchone()
        attachment[data[0]] = f'{clear_title}'
        connection.commit()

# attachment.append(clear_title)
# print(data[0])

cursor.close()
connection.close()
driver.close()

if attachment:
    with open('/tmp/list_movies.txt', 'w') as writer:
        writer.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
        <meta charset="utf-8">
        <style>
        </style>
    </head>
    <body>''')
        for key, value in attachment.items():
            writer.write(f'        <h1>{key}. {value}</h1>\n')
        writer.write('''    </body>
</html>''')

    file = open('/tmp/list_movies.txt')
    msg = file.read()

    msg = f'Subject: {sbj}\nFrom: {snd}\nTo: {rcv}\n'
    f'Content-Type: text/html\n{msg}'

    try:
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(snd, passwd)
        server.sendmail(snd, rcv, msg)
        server.close()
    except Exception as e:
        print("Failed to send the mail..", e)
