import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link='http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
    element.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    y = calc(x)

    z = browser.find_element_by_id("answer")
    z.send_keys(y)

    element2 = browser.find_element_by_xpath('//button[text()="Submit"]')
    element2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла