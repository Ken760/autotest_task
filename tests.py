from pages.yandex_search_page import SearchPage
from pages.yandex_images_page import ImagesPage

import allure


@allure.title("Поиск в яндексе")
def test_search_in_yandex(browser):
    yandex_search_page = SearchPage(browser)
    yandex_search_page.go_to_site('https://ya.ru/')
    with allure.step("Проверка наличия поиска"):
        yandex_search_page.search_in_yandex('Тензор')
    with allure.step("Проверка на то, что появилась таблица с подсказками (suggest)"):
        yandex_search_page.checking_suggest()
    with allure.step("При нажатии Enter появляется таблица результатов поиска"):
        yandex_search_page.click_on_the_search()
    with allure.step("Проверка, что появилась страница результатов поиска"):
        yandex_search_page.checking_search_results()
    with allure.step("Проверка на то, что первая ссылка ведет на tensor.ru"):
        yandex_search_page.checking_link_results()


@allure.title("Картинки на яндексе")
def test_yandex_images(browser):
    yandex_images_page = ImagesPage(browser)
    yandex_images_page .go_to_site('https://ya.ru/')
    with allure.step("Проверка присутсвия кнопки меню на странице"):
        yandex_images_page .checking_button_menu()
    with allure.step('Проверка открытия меню и перехода по ссылке'):
        yandex_images_page.open_menu_select_images()
    yandex_images_page.switch_to_page()
    with allure.step("Проверка перехода на url https://yandex.ru/images/"):
        yandex_images_page.checking_current_url()
    with allure.step("Проверка октрытия категории и текста в строке поиска"):
        yandex_images_page.selecting_theme_images()
    with allure.step("Проверка открытия первой картинку"):
        yandex_images_page.click_images()
    with allure.step("Проверка нажатия кнопки вперед картинка изменяется,"
                     "Проверка нажатия кнопки назад картинка изменяется на то же изображение"):
        yandex_images_page.check_images()