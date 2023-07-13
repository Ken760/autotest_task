from selenium.webdriver.common.by import By


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD = By.CSS_SELECTOR, '[class="search3__input mini-suggest__input"]'
    SUGGEST             = By.CLASS_NAME, "mini-suggest__popup-content"
    SEARCH_RESULTS      = By.XPATH, "//*[@class='serp-item serp-item_card']"


class YandexImagesLocators:
    MENU_BUTTON = By.XPATH, "//div[@class='services-suggest__icons-more']"
    YANDEX_IMAGE_LINK = (By.CSS_SELECTOR, "[aria-label='Картинки']")