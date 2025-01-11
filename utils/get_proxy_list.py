# Получение списка прокси
def get_proxy_list(proxy_path):
    with open(proxy_path, 'r') as file:
        proxies = file.read().split('\n')
        proxies = list(filter(lambda x: x!='', proxies))