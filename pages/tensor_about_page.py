from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TensorAboutPage(BasePage):
    ALL_PHOTOS_IN_WORKING_BLOCK = (By.XPATH, "//img[@class='tensor_ru-About__block3-image new_lazy loaded']")
    TOP_MANAGEMENT_BLOCK = (By.XPATH, "//p[@class='tensor_ru-header-h2 tensor_ru-pb-16' and text()='Топ-менеджмент']")

    def check_photos_for_the_size(self):
        assert self.is_url_match_to("https://tensor.ru/about")
        logger.info("Переход на страницу Тензор 'Подробнее' выполнен корректно")
        self.scroll_to_element(self.TOP_MANAGEMENT_BLOCK)
        all_photos_to_check = self.find_all(self.ALL_PHOTOS_IN_WORKING_BLOCK)
        logger.info("Проверка всех фотографий в блоке 'Работа в Тензоре' на соответствие размеру")
        for index, photo in enumerate(all_photos_to_check[:-1]):
            assert (all_photos_to_check[index].get_attribute("width")
                    == all_photos_to_check[index + 1].get_attribute("width"))
            assert (all_photos_to_check[index].get_attribute("height")
                    == all_photos_to_check[index + 1].get_attribute("height"))
        logger.info("Все фотографии в блоке 'Работа в Тензоре' соответствуют размеру")
