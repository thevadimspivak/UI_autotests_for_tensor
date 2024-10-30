"""
Второй сценарий:
1) Перейти на https://sbis.ru/ в раздел "Контакты"
2) Проверить, что определился ваш регион (в нашем примере
Ярославская обл.) и есть список партнеров.
3) Изменить регион на Камчатский край
4) Проверить, что подставился выбранный регион, список партнеров
изменился, url и title содержат информацию выбранного региона
"""
from pages.sbis_home_page import SbisHomePage


def test_second_scenario(driver):
    sbis_home_page = SbisHomePage(driver)
    sbis_contacts_page = sbis_home_page.go_to_contacts_page()
    sbis_contacts_page.check_if_my_region_is_defined()
    sbis_contacts_page.check_if_partners_are_presented()
    sbis_contacts_page.change_region()
    sbis_contacts_page.check_url_has_changed()
    sbis_contacts_page.check_partners_list_has_changed()