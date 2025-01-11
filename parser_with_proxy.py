import time
import requests
from bs4 import BeautifulSoup
import os

import get_data

from utils import choose_proxy, convert_csv_to_excel, get_proxy_list

from get_options import get_options


def main():
    proxy_list = get_proxy_list('proxy.txt')

    options = get_options()
    headers = options['headers']
    main_url = options['url']
    url = input('Сюда вставьте ваш url: ')

    working_proxy = choose_proxy(proxy_list, url, headers)

    try:
        req = requests.get(url, headers=headers, proxies=working_proxy )
        time.sleep(0.05)

    except Exception as e:
        with open('errors.log', 'a') as file:
            file.write(str(e))
            print(e)


    src = req.text
    soup = BeautifulSoup(src, 'lxml')

    type_sport = url.split('/')[3]

    urls = [main_url + i.get('href') for i in soup.find('div',
                                                                    class_='seo-links').find_all('a')]
    team = soup.find('div', class_='entity-header__info').find('div',
                                                                    class_='entity-header__title-name').find('a').text

    folder_name = team
    try:
        os.makedirs(f'data/{folder_name}')
    except:
        pass

    get_data(folder_name, urls, working_proxy, type_sport)
    convert_csv_to_excel(folder_name)

if __name__ == '__main__':
    main()
