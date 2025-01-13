from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


async def get_information_from_het():
    chromedriver_path = '/home/raxmatullox/Desktop/HET-Daily-Report-Bot-Private/chromedriver'
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get('https://cabinet.het.uz')
    wait = WebDriverWait(driver, 20)
    get_info, hash_information = """""", {}
    try:
        login_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="login"]')))
        login_field.send_keys('274040149141')

        password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]')))
        password_field.send_keys('Yc18jWXt')

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block')))
        login_button.click()


        wait.until(EC.url_to_be("https://cabinet.het.uz/household/home"))
        driver.get("https://cabinet.het.uz/household/home")

        ng_star_span = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-star-inserted')))
        for element in ng_star_span:
            try:
                if element.text != ' ' or '\n' or '':
                    get_info += element.text
                else: continue
            except: break
        print(get_info)

        # time.sleep(5)
    except TimeoutException: return 'Elementlar mavjud emas yoki kutish muddati tugadi!'
    finally: driver.quit() # quit browser

    hash = {}
    match = re.search(r"balansingiz \(oldindan to'lov\)(.*?)(?=Joriy oy)", get_info, re.DOTALL)
    amount = match.group(1).strip() if match else ""
    hash['amount'] = amount
    # print(hash)  # hisoblangan kVt·s

    match = re.search(r"hisoblangan kVt·s(.*?)(?=Joriy oy)", get_info, re.DOTALL)
    kv = match.group(1).strip() if match else ""
    hash['kv'] = kv
    # print(hash)

    match = re.search(r"hisoblangan summa(.*?)(?=Joriy oy)", get_info, re.DOTALL)
    sum = match.group(1).strip() if match else ""
    hash['sum'] = sum
    print(hash)

    match = re.search(r"To‘lov turi(.*?)(?=(current))", get_info, re.DOTALL)
    pay_sum = match.group(1).strip() if match else ""
    hash['sum'] = pay_sum
    # print(hash)
    print(pay_sum)

print(get_information_from_het())