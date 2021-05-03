from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def sum (x, y):
    return str(x + y)
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(2)

    # Ищем текст (значение атрибута)
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    # Считаем
    f = str(int(x)+int(y))
    print(f)

    # находим выпадающий список
    dropdown = browser.find_element_by_id("dropdown").click()

    # ищем элемент с текстом (сумма полученных чисел)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f)

    # находим кнопку "Отправить"
    input2 = browser.find_element_by_css_selector("button")
    input2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
