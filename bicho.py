from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# updateChromeDriver = Service(ChromeDriverManager().install())
# browser = webdriver.Chrome(service = driver)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# browser.get('https://www.ojogodobicho.com/deu_no_poste.htm')

# browser.find_element_by_xpath('/html/body/div[9]/div/div/div[1]/table/tbody/tr[1]/td[3]')
