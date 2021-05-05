from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(2)

    # Ищем значение х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # Считаем по формуле из предусловия
    f = calc(x)
    print(f)

    # скроллим страницу вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # ищем поле ввода
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f)

    # находим кнопку "чек-бокс"
    inputCheck = browser.find_element_by_id("robotCheckbox")
    inputCheck.click()

    # находим радио баттон
    inputRadio = browser.find_element_by_id("robotsRule")
    inputRadio.click()

    # находим кнопку "Отправить"
    input2 = browser.find_element_by_css_selector("button")
    input2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



