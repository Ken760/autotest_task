from pages.yandex_search_page import SearchPage

import allure


@allure.title("Поиск в яндексе")
def test_search_in_yandex(browser):
    yandex_main_page = SearchPage(browser)
    yandex_main_page.go_to_site('https://ya.ru/')
    with allure.step("Проверка наличия поиска"):
        yandex_main_page.search_in_yandex('Тензор')
    with allure.step("Проверка на то, что появилась таблица с подсказками (suggest)"):
        yandex_main_page.checking_suggest()
    with allure.step("При нажатии Enter появляется таблица результатов поиска"):
        yandex_main_page.click_on_the_search()
    with allure.step("Проверка, что появилась страница результатов поиска"):
        yandex_main_page.checking_search_results()
    with allure.step("Проверка на то, что первая ссылка ведет на tensor.ru"):
        yandex_main_page.checking_link_results()
