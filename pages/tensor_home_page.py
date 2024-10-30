from loguru import logger
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from pages.tensor_about_page import TensorAboutPage


class TensorHomePage(BasePage):
    STRENGTH_IN_PEOPLE_BLOCK = (By.XPATH, "//div[contains(@class, 'tensor_ru-Index__block4-content')"
                                          " and .//p[text()='Сила в людях']]")
    STRENGTH_IN_PEOPLE_ABOUT_LINK = (By.XPATH, "//a[@href='/about' and contains(@class, 'tensor_ru-link')]")

    def is_strength_in_people_block_presented(self):
        assert self.is_url_match_to("https://tensor.ru/")
        assert self.is_element_presented(self.STRENGTH_IN_PEOPLE_BLOCK) is True
        logger.info("Блок 'Сила в людях' присутствует на главной странице Тензор")

    def click_strength_in_people_about_link(self):
        self.click(self.STRENGTH_IN_PEOPLE_ABOUT_LINK)
        logger.info("Клик по ссылке 'Подробнее' в блоке Сила в людях")
        return TensorAboutPage(self.driver)




