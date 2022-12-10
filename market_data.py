from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from paths import url, values, headers, may_by_later_button
from utils import files_path
import time
import os
import csv

# opening the url
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)

# don't need to sign in 
try:
    may_by_later_button = driver.find_element(By.XPATH, may_by_later_button)
    may_by_later_button.click()
    print("click button")
except:
    print("pass")


headers = driver.find_elements(By.XPATH, headers)
header = []
for h in headers:
    header.append(h.text)
print(header)


# file path
path = os.getcwd()
csv_file_path = files_path(path)

# storing data into csv file
with open(csv_file_path, 'r+') as file:
    writer = csv.writer(file)
    header_exists = csv.reader(file)
    write_header = False
    for i in header_exists:
        if i == header:
            write_header = True
            break
    if write_header == False:
        writer.writerow(header)
    for i in range(10):
        values_list = []
        values_items = driver.find_elements(By.XPATH, values)
        for value in values_items:
            values_list.append(value.text)
        writer.writerow(values_list)
        time.sleep(5)
    file.close


# time.sleep(500)
driver.quit()