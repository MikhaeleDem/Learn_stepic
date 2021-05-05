from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # жмем на JS кнопку - анимашку
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    button.click()

    # определяем новое окно (которое появилось)
    new_window = browser.window_handles[1]
    # переключаемся на новое окно браузера
    browser.switch_to.window(new_window)

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




