import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
time.sleep(2)


def test_guest_should_see_login_link(browser):
    browser.get(link)
    # Проверяем, что элемент присутствует на странице
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "add_to_basket_form")))
