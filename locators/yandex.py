from selenium.webdriver.common.by import By


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD     = By.CSS_SELECTOR, '[class="search3__input mini-suggest__input"]'
    SUGGEST                 = By.CLASS_NAME, "mini-suggest__popup-content"
    SEARCH_RESULTS          = By.XPATH, "//*[@class='serp-item serp-item_card']"


class YandexImagesLocators:
    MENU_BUTTON             = By.XPATH, "//div[@class='services-suggest__icons-more']"
    YANDEX_IMAGE_LINK       = (By.CSS_SELECTOR, "[aria-label='Картинки']")
    SELECTING_IMAGES_THEME  = (By.CLASS_NAME, "PopularRequestList-Shadow")
    TITLE_THEME             = (By.CLASS_NAME, "PopularRequestList-SearchText")
    TEXT_INPUT              = (By.CLASS_NAME, "input__control")
    SELECTING_IMAGES        = (By.CLASS_NAME, "serp-item__link")
    NEXT_IMAGE_BUTTON       = (By.CLASS_NAME, "CircleButton_type_next")
    PREVIOUS_IMAGE_BUTTON   = (By.CLASS_NAME, "CircleButton_type_prev")