# прокоментировать код

import requests  # импорт библиотеки requests


# Функция возвращает список словарей, содержащих информацию о доступных странах
def get_list_of_available_countries() -> list[dict[str, str]]:
    url = 'https://date.nager.at/api/v3/AvailableCountries'  # ссылка на сайт
    response = requests.get(url).json()  # выполнение запроса

    return response  # возвращение параметра


# Функция преобразует список словарей в словарь, где ключ - название страны,
# а значение - код страны
def get_dict_of_countries_out_of_list(c: list[dict[str, str]]):
    result = dict()
    for country in c:
        result[country['name']] = country['countryCode']

    return result


# или однострочник
# def get_dict_of_countries_out_of_list(c: list[dict[str, str]]):
# return dict((country['name'], country['countryCode']) for country in c)


def main() -> None:
    # Получаем список стран и преобразуем его в словарь
    list_of_countries = get_list_of_available_countries()
    dict_of_countries = get_dict_of_countries_out_of_list(list_of_countries)

    # Проверяем наличие страны Russia в словаре
    if 'Russia' in dict_of_countries:
        print(f'Страна Russia, код [{dict_of_countries["Russia"]}]')
    else:
        print(f"Страна Russia не найдена")


# Условие для выполнения main() только при запуске скрипта напрямую
if __name__ == '__main__':
    main()
