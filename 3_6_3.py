import time
import math
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Данный фикстур - стандартная конструкция запуска браузера перед каждым тестом и закрытие, после прохождения
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Создаем фикстур пере классом, чтобы поочередно подставить значение переменной URL из массива, которые она примет
@pytest.mark.parametrize('URL', ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
class TestMainPage1:
    def test_guest(self, browser, URL):
    # Указываем, что линк это переменная, указанная перед классом, массивом
        link = f"{URL}/"

        browser.get(link)
        time.sleep(10)
        browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']").send_keys(str(math.log(int(time.time()))))
        button1 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button1.click()
        time.sleep(10)
        textOK_elt = browser.find_element_by_class_name("smart-hints__hint")
        textOK = textOK_elt.text
        exceptedText = "Correct!"
        assert textOK == exceptedText, f"expected {exceptedText}, got {textOK}"







