import requests

from data import config

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (HTML, like Gecko) "
                  "Chrome/47.0.2526.106 Safari/537.36"
}

news_url = config.api_url_news_ru

r = requests.get(news_url, headers=headers)

print(r.status_code)
n = r.json()
print(type(n))

l = n.get('rows')
print(type(l))


# for d in l:
#     for k in d:
#         print(f'{k} : {d[k]}')
#     print('\n\n\n')