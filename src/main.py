from selenium import webdriver
import time

# Create the variables that contains the website and the ZIP code
WEBSITE = "https://www.siterastreio.com.br/cep"
ZIP_CODE = "02762-060"

# Initiallize the webdriver and the browser
browser = webdriver.Edge()
browser.get(WEBSITE)
time.sleep(3)

# Input the ZIP code value on the input box
inputCep = browser.find_element('xpath', '/html/body/section[1]/div/div/div[1]/div/input')
inputCep.send_keys(ZIP_CODE)
time.sleep(2)

# Confirm the ZIP code search on the website and return the ZIP code informations on the user's screen
confirmSearch = browser.find_element('xpath', '/html/body/section[1]/div/div/div[1]/div/a/button')
confirmSearch.click()
time.sleep(5)