
def get_options():
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 '
                        'Firefox/115.0'
    }

    main_url = 'https://www.championat.com/'

    options = {'headers': headers, 'url': main_url}
    return options