from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд

    browser.get(link)
    # ждем нужное значение у таймера обратного отсчета
    button1 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print(button1)
    # когда нужное значение дождались - кликаем на кнопку
    button = browser.find_element_by_id("book")
    button.click()


    # Ищем значение х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # Считаем по формуле из предусловия
    f = calc(x)
    print(f)

    # ищем поле ввода
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f)

    # находим кнопку "Отправить"
    input2 = browser.find_element_by_id("solve")
    input2.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




