from selenium import webdriver
import time

# Create the variables that contains the website and the CEP
WEBSITE = "https://www.siterastreio.com.br/cep"
CEP = "02762-060"

# Initiallize the webdriver and the browser
browser = webdriver.Edge()
browser.get(WEBSITE)
time.sleep(3)

# Input the CEP value on the input box
inputCep = browser.find_element('xpath', '/html/body/section[1]/div/div/div[1]/div/input')
inputCep.send_keys(CEP)
time.sleep(2)

# Confirm the CEP search on the website and return the cep informations on the user's screen
confirmSearch = browser.find_element('xpath', '/html/body/section[1]/div/div/div[1]/div/a/button')
confirmSearch.click()
time.sleep(5)