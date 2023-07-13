from .base_page import BasePage
from time import sleep
from locators.yandex import YandexImagesLocators, YandexSearchLocators


class ImagesPage(BasePage):

    def checking_button_menu(self):
        """Проверка кнопки меню"""
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD).click()
        assert self.is_element_present(*YandexImagesLocators.MENU_BUTTON), "Ссылка на картинки отсутствует"

    def switch_to_page(self):
        """Переключение на другое окно браузера"""
        tabs = self.browser.window_handles  # список отрывшихся вкладок
        self.browser.switch_to.window(tabs[1])

    def open_menu_select_images(self):
        """Проверка открытия и перехода на картинки"""
        menu_button = self.browser.find_element(*YandexImagesLocators.MENU_BUTTON).click()
        sleep(1)
        images_link = self.browser.find_element(*YandexImagesLocators.YANDEX_IMAGE_LINK)
        images_link.click()
        sleep(5)

    def checking_current_url(self):
        """Проверка перехода на url"""
        assert "https://yandex.ru/images/" in self.browser.current_url, 'Некорректный url'

    # def switch_to_page(self):
    #     """Переключение на другое окно браузера"""
    #     tabs = self.browser.window_handles  # список отрывшихся вкладок
    #     self.browser.switch_to.window(tabs[1])
    #
    # def checking_current_url(self):
    #     """Проверка перехода на url"""
    #     assert "https://yandex.ru/images/" in self.browser.current_url, 'Некорректный url'