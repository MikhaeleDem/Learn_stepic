from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим кнопку "Отправить"
    input1 = browser.find_element_by_tag_name("button")
    input1.click()

    # Нажимаем ОК в появившемся алерте
    alert = browser.switch_to.alert
    alert.accept()

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
    input2 = browser.find_element_by_css_selector("button")
    input2.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




