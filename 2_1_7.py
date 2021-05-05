from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем текс (значение атрибута) у картинки
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    # находим поле ввода
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # находим чек-бокс
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