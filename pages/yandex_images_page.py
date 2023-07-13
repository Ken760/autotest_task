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

    def checking_current_url(self):
        """Проверка перехода на url"""
        assert "https://yandex.ru/images/" in self.browser.current_url, 'Некорректный url'

    def selecting_theme_images(self):
        """Открытие первой категории"""
        images_theme = self.browser.find_elements(*YandexImagesLocators.SELECTING_IMAGES_THEME)
        selecting_images_theme = images_theme[0].click() # Выбор темы изображения
        sleep(1)

    def title_check_in_search(self):
        """Проверка названия категории в поиске"""
        title_theme = self.browser.find_element(*YandexImagesLocators.TITLE_THEME).text
        input_text = self.browser.find_element(*YandexImagesLocators.TEXT_INPUT).get_attribute('value')
        assert title_theme in input_text, "Название категории не отображается в поле поиска"

    def click_images(self):
        """Проверка на открытие первой картинки"""
        assert self.is_element_present(*YandexImagesLocators.SELECTING_IMAGES), \
            "Картинка отсутствует, страница не открылась"
        images = self.browser.find_elements(*YandexImagesLocators.SELECTING_IMAGES)
        selecting_images = images[0]  # Выбор картинки
        selecting_images.click()
        sleep(1)

    def check_images(self):
        """Проверка на совпадение изображений"""
        img_url = self.browser.current_url
        self.button_next_images()
        self.button_previous_images()
        assert self.browser.current_url in img_url, "Изображения не совпадают"

    def button_next_images(self):
        """Кнопка выбора следущей картинки"""
        assert self.is_element_present(*YandexImagesLocators.NEXT_IMAGE_BUTTON), \
            "Кнопка следущего картинки отсутствует"
        next_button = self.browser.find_element(*YandexImagesLocators.NEXT_IMAGE_BUTTON)
        next_button.click()
        sleep(1)

    def button_previous_images(self):
        """Кнопка выбора предыдущей картинки"""
        assert self.is_element_present(*YandexImagesLocators.PREVIOUS_IMAGE_BUTTON), \
            "Кнопка предыдущего картинки     отсутствует"
        prev_button = self.browser.find_element(*YandexImagesLocators.PREVIOUS_IMAGE_BUTTON)
        prev_button.click()
        sleep(1)