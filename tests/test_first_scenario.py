"""
Первый сценарий:
1) Перейти на https://sbis.ru/ в раздел "Контакты"
2) Найти баннер Тензор, кликнуть по нему
3) Перейти на https://tensor.ru/
4) Проверить, что есть блок "Сила в людях"
5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
https://tensor.ru/about
6) Находим раздел Работаем и проверяем, что у всех фотографии
хронологии одинаковые высота (height) и ширина (width)
"""
from pages.sbis_home_page import SbisHomePage


def test_first_scenario(driver):
    sbis_home_page = SbisHomePage(driver)
    sbis_contacts_page = sbis_home_page.go_to_contacts_page()
    tensor_home_page = sbis_contacts_page.clink_tensor_banner()
    tensor_home_page.is_strength_in_people_block_presented()
    tensor_about_page = tensor_home_page.click_strength_in_people_about_link()
    tensor_about_page.check_photos_for_the_size()




