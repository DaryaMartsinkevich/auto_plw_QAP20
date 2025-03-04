# Запуск браузера
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)     #Запуск браузера
    page = browser.new_page()
    page.goto('https://example.com')
    print(page.title())     #Вывод заголовка старницы
    browser.close()         #Закрытие страницы

# Откртытие страницы и навигации
page.goto('https://example.com')
page.reload()       #Перезагрузка страницы
page.go_back()      #Назад
page.go_forward()       #Вперед

# Локаторы элементов
element = page.locator('css=button')        #CSS-селектор
element = page.locator('text="Купить"')     #По тексту
element = page.locator("//button[@id='submit']")    #XPath


#Клики и ввод текста
page.locator('#login-button').click()       #Клик по кнопке
page.locator('#username').fill("test_user")     #Ввод текста
page.locator('#password').type('secure_password')       #Поэтапный ввод


#Работа с формами
page.locator("form").press('Enter')     #Отправка формы через Enter
page.locator("#submit").click()     #НАжатие на кропку отправки


#Проверка наличия элемента
assert page.locator("#success-message").is_visible()