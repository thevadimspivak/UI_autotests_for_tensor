from loguru import logger
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.tensor_home_page import TensorHomePage


class SbisContactsPage(BasePage):

    TENSOR_BANNER = (By.XPATH, "//a[@class='sbisru-Contacts__logo-tensor mb-12']")
    REGION_BUTTON = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link'][1]")
    PARTNERS_CITY_ID = (By.XPATH, "//div[@id='city-id-2']")
    PARTNERS_LIST = (By.XPATH, "(//div[contains(@class, 'controls-BaseControl') "
                               "and contains(@class, 'controls_list_theme-sbisru')])[1]")
    REGION_TO_BE_CHANGED = (By.XPATH, "//span[text()='41 Камчатский край']")

    def clink_tensor_banner(self):
        self.new_tab_click(self.TENSOR_BANNER)
        logger.info('Успешный клик на баннер Тензор.')
        return TensorHomePage(self.driver)

    def check_if_my_region_is_defined(self):
        my_region = "Республика Башкортостан"
        logger.info("Проверка на соответствие региону, который определился автоматически")
        assert self.get_text(self.REGION_BUTTON) == my_region
        logger.info(f"Регион определился корректно: {my_region}")

    def check_if_partners_are_presented(self):
        assert self.is_element_presented(self.PARTNERS_LIST) is True
        logger.info("Список партнеров присутствует на странице Контакты")
        assert self.get_text(self.PARTNERS_CITY_ID) == "Уфа"
        logger.info("Город Уфа присутствует в списке партнеров")

    def change_region(self):
        self.click(self.REGION_BUTTON)
        self.click(self.REGION_TO_BE_CHANGED)
        logger.info("Регион успешно изменен на '41 Камчатский край'")

    def check_url_has_changed(self):
        kamchatka_text_in_path = "41-kamchatskij-kraj"
        assert self.is_url_contains(kamchatka_text_in_path)
        logger.info("URL успешно изменён и содержит текст '41-kamchatskij-kraj'")

    def check_partners_list_has_changed(self):
        assert self.get_text(self.PARTNERS_CITY_ID) == "Петропавловск-Камчатский"
        logger.info("Список партнеров успешно изменён. Теперь в списке партнеров город Петропавловск-Камчатский")


