from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import random

load_more_click_num = 20
implicit_wait_time = 30
account_num = 1
download_fd = 'D:\\GoogleDnwd\\'

option = webdriver.ChromeOptions()
# Type chrom://version/ in Chrome browser to get the profile path
option.add_argument('--user-data-dir=C:\\Users\\22920\\AppData\\Local\\Google\\Chrome\\User Data\\')
option.add_argument('blink-settings=imagesEnabled=false')
# option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(implicit_wait_time)

# First, for every account, run dump_cookies.py and login manually in Chrome browser
# If successful, you will see the cookies.pkl file in the same directory
# Rename it and throw it into the cookies directory

# Load Index
# Maintain the index.txt file in the same directory
last_index = 0
try:
    with open('index.txt', 'r') as index_file:
        last_index = int(index_file.read().strip())
        print("Last Index: " + str(last_index))
except FileNotFoundError:
    last_index = 0

# for i in range(account_num):
for i in range(0, 49):
    load_more_click_num = last_index // 64 + 4
    print("Load More Click Num: " + str(load_more_click_num))
    print("Account: " + str(i))
    driver.get("https://3dwarehouse.sketchup.com/search/products")
    cookies = pickle.load(open(".\\cookies\\cookies" + "_" + str(i) + ".pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    time.sleep(1)

    for _ in range(1, load_more_click_num):
        load_more_button = driver.find_element('css selector', 'button[data-cy="load-more-button"]:not([disabled])')
        if load_more_button:
            load_more_button.click()
        else:
            break

    time.sleep(1)

    driver.find_element('tag name', 'body').send_keys(Keys.HOME)

    search_results = driver.find_elements("class name", "search-results__content-card")

    cnt = 0
    for j, search_result in enumerate(search_results):
        if j < last_index:
            continue

        download_button = search_result.find_element('css selector', "button.btn.primary-btn.icon")
        if download_button:
            # driver.execute_script("arguments[0].scrollIntoView();", download_button)
            download_button.click()

            div_element = driver.find_element("css selector", ".p-menu.p-component.p-menu-overlay.p-ripple-disabled")

            if div_element:
                try: 
                    data_cy_val = "download-menu-zip"
                    last_button = div_element.find_element('css selector', f'button[data-cy="{data_cy_val}"]')
                    if last_button:
                        wait_interval = random.randint(4, 8)
                        last_button.click()
                        time.sleep(wait_interval)

                    print("Index :" + str(j))
                except:
                    continue
        cnt += 1
        if cnt == 100:
            last_index = j + 1
            break

    with open('index.txt', 'w') as index_file:
        index_file.write(str(last_index))

driver.quit()