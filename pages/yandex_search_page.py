from selenium.webdriver import Keys
from .base_page import BasePage
from locators.yaru import YandexSearchLocators


class SearchPage(BasePage):

    def search_in_yandex(self, word):
        """
        Ввод в поле поиска текста запроса
        :param word: текст запроса
        """
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_FIELD), 'Поле поиска отсутсвует'
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)

    def checking_suggest(self):
        """Проверка таблицы с подсказками"""
        assert self.is_element_present(*YandexSearchLocators.SUGGEST), 'Таблица с подсказками отсутствует'

    def click_on_the_search(self):
        """Нажатие кнопки enter"""
        pressing_enter = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        pressing_enter.send_keys(Keys.ENTER)

    def checking_search_results(self):
        """Проверка результатов поиска"""
        assert self.is_element_present(
            *YandexSearchLocators.SEARCH_RESULTS), 'Страница результатов поиска не появилась'


    def checking_link_results(self):
        """Проверка первой первой ссылки"""
        link = self.browser.find_elements(*YandexSearchLocators.SEARCH_RESULTS)[0].text
        assert 'tensor.ru' in link, 'Сылка не ведет на сайт tensor.ru'
