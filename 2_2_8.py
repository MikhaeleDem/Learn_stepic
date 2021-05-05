from selenium import webdriver
import time
import os



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input:nth-child(2)")
    input1.send_keys("Михаил")
    input2 = browser.find_element_by_css_selector("input:nth-child(4)")
    input2.send_keys("Смирнов")
    input3 = browser.find_element_by_css_selector("input:nth-child(6)")
    input3.send_keys("m@mail.ru")

    # получаем путь к дерриктории с файлом
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    # находим кнопку загрузки файла
    load = browser.find_element_by_id("file")
    load.send_keys(file_path)
    # находим кнопку "Отправить"
    input2 = browser.find_element_by_css_selector("button")
    input2.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




