"""
Третий сценарий (необязательный):
1) Перейти на https://sbis.ru/
2) В Footer'e найти и перейти "Скачать СБИС"
3) Скачать СБИС Плагин для вашей для windows, веб-установщик в
папку с данным тестом
4) Убедиться, что плагин скачался
5) Сравнить размер скачанного файла в мегабайтах. Он должен
совпадать с указанным на сайте (в примере 3.64 МБ).
"""
from pages.sbis_home_page import SbisHomePage


def test_third_scenario(driver):
    sbis_home_page = SbisHomePage(driver)
    sbis_download_page = sbis_home_page.go_to_download_page()
    sbis_download_page.is_right_plugin_is_tab_selected()
    sbis_download_page.check_windows_tab()
    sbis_download_page.download_exe_file()
    sbis_download_page.is_app_size_correct()
    sbis_download_page.delete_downloaded_file()
