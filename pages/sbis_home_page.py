from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.sbis_contacts_page import SbisContactsPage
from loguru import logger

from pages.sbis_download_page import SbisDownloadPage


class SbisHomePage(BasePage):

    START_WORK_BUTTON = (By.XPATH, "//button[@id='header-menu-btn']")
    BURGER_MENU = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'burger')]")
    TARIFFS_BUTTON = (By.XPATH, "//a[contains(@class, 'sbisru-Header__menu-link') and @href='/tariffs']")
    OPENS_CONTACTS_MODAL_WINDOW = (By.XPATH, "//*[contains(@class, 'sbisru-Header__menu-link') and text()='Контакты']")
    CONTACTS_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'sbisru-Header-ContactsMenu__items')]")
    CONTACTS_LINK = (By.XPATH, "//*[contains(@class, 'sbisru-link') and @href='/contacts']")
    BLOG_BUTTON = (By.XPATH, "//a[contains(@class, 'sbisru-Header__menu-link') and @href='/articles']")
    SUPPORT_BUTTON = (By.XPATH, "//a[contains(@class, 'sbisru-Header__menu-link') and @href='/support']")
    CLIENT_CHAT_WIDGET_BUTTON = (By.XPATH, "//div[@title='Кнопка вызова']")
    SBIS_DOWNLOAD_LINK = (By.LINK_TEXT, "Скачать локальные версии")

    def go_to_contacts_page(self):
        logger.info("Открытие модального окна контактов")
        self.click(self.OPENS_CONTACTS_MODAL_WINDOW)
        logger.info("Ожидание появления модального окна контактов")
        self.wait_until_element_is_visible(self.CONTACTS_MODAL_WINDOW)
        logger.info("Переход на страницу контактов")
        self.click(self.CONTACTS_LINK)
        logger.info("Успешный переход на страницу контактов")
        return SbisContactsPage(self.driver)

    def go_to_download_page(self):
        self.click(self.SBIS_DOWNLOAD_LINK)
        logger.info("Переход на страницу скачивания приложения SBIS")
        return SbisDownloadPage(self.driver)





