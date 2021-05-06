import time
import unittest
from selenium import webdriver


class Test123(unittest.TestCase):
    def bodyOfTest(self, link):
        exceptedText = "Congratulations! You have successfully registered!"
        browser = webdriver.Chrome()

        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        time.sleep(2)
        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Михаил")
        input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        input2.send_keys("Смирнов")
        input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input3.send_keys("m@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(exceptedText, welcome_text,
                         '''Excepted value:{}
                    Actuqal value:{}'''.format(exceptedText, welcome_text))

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test1(self):
        self.bodyOfTest("http://suninjuly.github.io/registration1.html")

    def test2(self):
        self.bodyOfTest("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__": unittest.main()
