import wget
import os

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def find(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
        except NoSuchElementException:
            print(f"Элемент {locator} не найден на странице")

    def find_by_text(self, text):
        return self.find((By.XPATH, f"//*/text()[contains(.,'{text}')]"))

    def find_all(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def get_text(self, locator):
        return self.find(locator).text

    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def new_tab_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_url_match_to(self, url):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(url)
            )
            return True
        except TimeoutException:
            return False

    def is_url_contains(self, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False

    def wait_until_element_is_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def is_element_presented(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException or NoSuchElementException:
            return False

    def download_file(self, link):
        wget.download(link, os.getcwd())
