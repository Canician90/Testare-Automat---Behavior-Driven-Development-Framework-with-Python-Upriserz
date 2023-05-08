# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/alerts')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva


# completam username in f de atribuit=valoare

chrome.find_element(By.ID, 'alertButton"]').click()

chrome.switch_to.alert.accept()




# verifica
# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')

# fail