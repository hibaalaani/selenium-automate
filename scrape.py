from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from csv import reader
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# import xlrd
import csv
chrome_options = Options()
chrome_options.add_extension('snapaddy.crx.crx')
driver = webdriver.Chrome(
    '/home/logicrays/Downloads/chromedriver', chrome_options=chrome_options)
url = 'https://www.google.com'

print('\nInitializing...')


# driver= webdriver.Chrome()
driver.implicitly_wait(2)
driver.get(url)

driver.implicitly_wait(3)
sleep(3)
# driver.fullscreen_window()


with open("list.csv", 'r') as file_obj:
    csv_reader = reader(file_obj)

    for row in csv_reader:
        pages = row[2]

        print(row[0])
        if csv_reader.line_num == 1:
            continue

        append_key = row[0] + ' ' + row[1]
        search = driver.find_element_by_css_selector(".gLFyf.gsfi")
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(append_key)

        search.send_keys(Keys.RETURN)
        sleep(5)

try:
    snapaddy_icons = driver.find_elements_by_css_selector(
        ".grabber-btn")
    print(len(snapaddy_icons))
    for s in snapaddy_icons:
        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)
        print(s)
        s.click()
        sleep(5)
        # Switch to newly opened window
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        sleep(2)
    try:
        driver.find_element_by_css_selector("#btn-login")
        email_input = driver.find_element_by_css_selector(
            "body > snapaddy-grabber > div.angular-wrapper > main > div > div > div > div > div.form-group > div:nth-child(1) > input")
        email_input.send_keys("kcol@mailpoly.xyz")
        pwd_input = driver.find_element_by_css_selector(
            "body > snapaddy-grabber > div.angular-wrapper > main > div > div > div > div > div.form-group > div:nth-child(2) > input")
        pwd_input.send_keys("kcol@mailpoly.xyz1")
        driver.find_element_by_css_selector("#btn-login").click()
