import pytest
from selenium import webdriver
from loguru import logger


@pytest.fixture(params=["chrome", "firefox", "edge"])
# @pytest.fixture(params=["chrome", "edge"])
def driver(request):
    browser = request.param
    logger.add(f"./logs/logs_{browser}.log", format="{time:YYYY-MM-DD at HH:mm:ss!UTC} | {level} | {message}",
               rotation="1 day", compression="zip")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unknown browser")
    driver.get("https://sbis.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()


