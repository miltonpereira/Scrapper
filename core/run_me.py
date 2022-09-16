""" running the base url """

import time
import main_script_file


PG_NO = 10
TOTAL_PAGES = 40

while PG_NO <= TOTAL_PAGES:
    BASE_URL = "https://www.google.co.in"
    KEY_WORD = ('QA Companies')
    payload = {'q': KEY_WORD, 'start': PG_NO}
    data = main_script_file.fetch_html(BASE_URL, payload)
    FINAL_DATA = main_script_file.parse_and_scrape_data(data)
    PG_NO = PG_NO + 10
    time.sleep(60)
print('Your script has been executed! Bye')
