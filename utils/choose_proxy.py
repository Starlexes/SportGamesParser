import requests

# Выбор работающего прокси
def choose_proxy(proxies, url, headers):
    for proxy in proxies:
        try:
            proxy = {'http': proxy}

            req = requests.get(url, headers=headers, proxies=proxy, timeout=4)
            if req.status_code == 200:
                break

        except Exception as e:
            print(e)
            continue
    return proxy