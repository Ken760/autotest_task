from selenium.webdriver.common.by import By


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD = By.CSS_SELECTOR, '[class="search3__input mini-suggest__input"]'
    SUGGEST             = By.CLASS_NAME, "mini-suggest__popup_visible" # class="mini-suggest__popup-content"
    RESULTS_TABLE       = By.CSS_SELECTOR, '[class="organic__title-wrapper typo typo_text_l typo_line_m"]'
    SEARCH_RESULTS      = By.CLASS_NAME, "OrganicTitleContentSpan organic__title"