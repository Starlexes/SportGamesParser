import requests
import json
import time
from bs4 import BeautifulSoup
import csv

from get_options import get_options

# Основной парсер
def get_data(folder_name, urls, proxies, type_sport):
    with open(f'data/{folder_name}/data.csv', 'a', newline='') as file:
        writer = csv.writer(file)


        writer.writerow(['Вид спорта', 'Название команды', 'Год игр', 'Название турнира', 'Тур',
                         'Дата', 'Матч', 'Счет'])
    main_ct = 1 # текущее число загруженных данных
    options = get_options()
    headers = options['headers']
    
    for url in urls:

        try:
            req = requests.get(url, headers=headers, proxies=proxies)
            time.sleep(0.05)
        except Exception as e:
            with open('errors.log', 'a') as file:
                file.write(str(e))
                print(e)


        src = req.text
        soup = BeautifulSoup(src, 'lxml')

        code = url.split('/')[7]

        t = soup.find('script', class_='js-entity-header-select-data').text.strip()
        json_data = json.loads(t)
        year = "Нет данных"
        tournement = "Нет данных"
        for d in json_data:

            if d['data']:
                for i in d['data']:
                    if i['label'] == code:
                       tournement = i['title']
                       year = d['label']
                       break

        team = soup.find('div', class_='entity-header__info').find('div',
                                                                      class_='entity-header__title-name').find('a').text

        try:
            matches = soup.find('div', class_='js-tournament-filter-content').find_all('tr',class_='stat-results__row js-tournament-filter-row')
        except AttributeError:
            matches = "Нет данных"

        if matches != "Нет данных":
            for match in matches:

                date = match.find('td', class_='stat-results__date-time _hidden-td').text

                tour = match['data-tour'] if match['data-tour'] else 'Нет данных'

                mat = [i.text for i in match.find('div', class_='stat-results__title-teams '
                                                              '_margin-fav').find_all(
                    'span', class_='table-item__name')]

                mat = f'{mat[0]} - {mat[1]}'
                count = match.find('td', class_='stat-results__count _center').find('span').text.strip()

                info = [tour, date, mat, count]
                counter = 1
                with open(f'data/{folder_name}/data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)

                    if counter == 1:
                        writer.writerow([type_sport, team, year, tournement, info[0], info[1], info[2],
                                         info[3]])
                    else:
                        writer.writerow(['', '', '', '', info[0], info[1], info[2],
                                         info[3]])
                counter+=1

        print(f"Загружено данных {main_ct}/{len(urls)}")
        main_ct += 1
    with open(f'data/{folder_name}/data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['', '', '', ''])

    counter = 1