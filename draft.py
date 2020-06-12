import requests

urls = ['https://google.com', 'https://yandex.ru',
        'https://youtube.com', 'https://onliner.by',
        'https://www.weblancer.net', 'https://hwschool.online']

for url in urls:
    target = requests.get(url)
    for i in range(200):
        # print(url, i, target.status_code)
        if target.status_code != 200:
            print(url, i, target.status_code)
