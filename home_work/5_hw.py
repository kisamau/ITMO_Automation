from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

def elements_on_page():
    driver.get("https://www.saucedemo.com/")
    username_block = driver.find_element(By.ID, 'user-name')
    password_block = driver.find_element(By.ID, 'password')
    submit_button = driver.find_element(By.ID, 'login-button')
    if username_block and password_block and submit_button is None:
        print('error')
    else:
        print('Элементы найдены')
elements_on_page()