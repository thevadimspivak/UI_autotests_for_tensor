import os
import re
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SbisDownloadPage(BasePage):
    SBIS_PLUGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'controls-TabButton') and @data-id='plugin']")
    OS_WINDOWS_TAB = (By.XPATH, "//span[contains(@class, 'sbis_ru-DownloadNew') and text()='Windows']")
    OS_MAC_TAB = (By.XPATH, "//span[contains(@class, 'sbis_ru-DownloadNew') and text()='MacOS']")
    OS_LINUX_TAB = (By.XPATH, "//span[contains(@class, 'sbis_ru-DownloadNew') and text()='Linux']")
    WINDOWS_WEB_INSTALLER_LINK = (By.XPATH, "//a[contains(text(), 'Скачать (Exe')]")

    def is_right_plugin_is_tab_selected(self):
        plugin_tab = self.find(self.SBIS_PLUGIN_BUTTON)
        assert "controls-Checked__checked" in plugin_tab.get_attribute("class")
        logger.info("Вкладка 'СБИС Плагин' выбрана корректно")

    def check_windows_tab(self):
        self.click(self.OS_WINDOWS_TAB)
        logger.info("Выбрана вкладка 'Windows' для скачивания приложения")

    def find_app_size(self):
        app_size = self.get_text(self.WINDOWS_WEB_INSTALLER_LINK)
        size = re.findall(r'\d+', app_size)
        size = float('{}.{}'.format(size[0], size[1]))
        logger.info(f"Размер файла приложения должен быть {size} МБ")
        return size

    def download_exe_file(self):
        app_link = self.find(self.WINDOWS_WEB_INSTALLER_LINK).get_attribute("href")
        self.download_file(app_link)
        logger.info("Скачивание приложения для Windows завершено")

    def is_app_size_correct(self):
        download_app_path = os.getcwd() + "/sbisplugin-setup-web.exe"
        download_app_size = round(os.path.getsize(download_app_path) / 1048576, 2)
        assert download_app_size == self.find_app_size()
        logger.info("Размер скачанного файла приложения соответствует ожидаемому")

    def delete_downloaded_file(self):
        download_app_path = os.getcwd() + "/sbisplugin-setup-web.exe"
        while True:
            try:
                os.remove(download_app_path)
                break
            except PermissionError:
                sleep(1)
        logger.info("Скачанный файл был удалён")

