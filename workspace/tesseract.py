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


from PIL import Image
from io import BytesIO
from pytesseract import pytesseract

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(
    options=chrome_options,
    service=Service(ChromeDriverManager().install())
)
driver.get('https://rarbgproxied.org/torrents.php')
driver.implicitly_wait(10) # seconds
driver.save_screenshot('screenshot.png')
from pdb import set_trace; set_trace()
# image_bytes = driver.find_element(By.ID, "logo-icon").screenshot_as_png
# image = Image.open(BytesIO(image_bytes)).save('output.png')
# text = pytesseract.image_to_string(Image.open(BytesIO(image_bytes)))


driver.close()
