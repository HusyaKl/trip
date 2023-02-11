import requests
from bs4 import BeautifulSoup as BS
from dataclasses import dataclass
import json
import pandas
from . import models


@dataclass
class Place:
  category: str
  name: str
  description: str
  metro_station: str
  address: str
  coordinates: tuple


def parse(relative_url) -> Place:
  '''
    Given relative url
    Returns category, name, description, metro station, address, coordinates
    >>> parse('kofeynya_1981/92363235284/')
    Place(category='coffee_shop', name='Кофейня 1981', description='Кухня:европейская, русская, азиатская, домашняя, смешанная', metro_station='Стахановская', address='Москва, 2-й Грайвороновский проезд, 44, корп. 1', coordinates=(55.726041, 37.745663))
    '''
  cookies = {
    'maps_los': '0',
    'yandexuid': '2797350221662382980',
    'yuidss': '2797350221662382980',
    'gdpr': '0',
    '_ym_uid': '1652702309554603674',
    'ymex': '1977742996.yrts.1662382996#1977767281.yrtsi.1662407281',
    'font_loaded': 'YSv1',
    'my': 'YwA=',
    '_ym_d': '1670147721',
    'tmr_lvid': '91937e083617052a09d5b73da33aba62',
    'tmr_lvidTS': '1670240683142',
    'i':
    'S6qDcBpMZxxJh8qVUHBHKbHZmeKzPHcEM/QAHfPYetwglmsAZ8LCvGYJpKuWGm6f5nlPO93rEwyr+F8NBwRpH2sU4gc=',
    'yashr': '9919303011674047544',
    'yabs-frequency':
    '/5/0G00020Zn6C00000/yTwHdct3rboCIY6gLHYeSrvqPunA8O6f6ZyhvZvRZ4f0lmdSQgKlb5ICIa00/',
    'L':
    'ZnJHaV94U1libXpQV3d9VlpKRERmaXVxORMYJiYtOg==.1674854447.15235.397660.d25b15a3a68213f47456581aafc75b5f',
    'is_gdpr': '0',
    'is_gdpr_b': 'CPvaURCapAEoAg==',
    'maps_routes_travel_mode': 'auto',
    'cycada': '/LaYUrzbQEatO+xXJznxP/cNhiWPHtw2YcnuHQqC1hU=',
    'Session_id':
    '3:1675968494.5.0.1674854447144:oDPcTQ:2b.1.2:1|696647019.0.2|3:10265343.31607.S-bSsTfP0UFZxNpDSzcS5Ln3CW4',
    'sessionid2':
    '3:1675968494.5.0.1674854447144:oDPcTQ:2b.1.2:1|696647019.0.2|3:10265343.31607.fakesign0000000000000000000',
    'sae':
    '0:8c5b9e54-9e52-4d6f-83a4-a3c0450C13C0:p:22.11.3.838:l:d:RU:20220516',
    'ys':
    'svt.1#def_bro.0#wprid.1676118199745950-12193408649448493562-sas3-0824-95c-sas-l7-balancer-8080-BAL-7430#ybzcc.ru#newsca.native_cache',
    '_yasc':
    'lO3JsWln68wj9jMUo/BtNxbDMD8r2gQJH5WZXpS9TFQNcGy1mfane7ZQCsnC0ra07bsH006FzmE3Kw==',
    'yp':
    '1676204487.uc.ru#1676204487.duc.ru#1705126405.cld.2574584#1991478201.pcs.0#1690782929.szm.1:1920x1080:1872x938#1677939461.csc.1#1990214447.udn.cDphcmtsdWFs#1676723001.mcv.0#1676723001.mcl.d2uoyx',
    '_ym_isad': '2',
  }

  headers = {
    'authority':
    'yandex.ru',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':
    'ru,en;q=0.9',
    'cache-control':
    'max-age=0',
    'referer':
    'https://www.yandex.ru/clck/jsredir?from=yandex.ru;suggest;browser&text=',
    'sec-ch-ua':
    '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
    'sec-ch-ua-arch':
    '"x86"',
    'sec-ch-ua-bitness':
    '"64"',
    'sec-ch-ua-full-version':
    '"22.11.3.838"',
    'sec-ch-ua-full-version-list':
    '"Chromium";v="106.0.5249.199", "Yandex";v="22.11.3.838", "Not;A=Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-model':
    '""',
    'sec-ch-ua-platform':
    '"Linux"',
    'sec-ch-ua-platform-version':
    '"6.0.15"',
    'sec-fetch-dest':
    'document',
    'sec-fetch-mode':
    'navigate',
    'sec-fetch-site':
    'same-origin',
    'sec-fetch-user':
    '?1',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.838 Yowser/2.5 Safari/537.36',
  }

  response = requests.get(f'https://yandex.ru/maps/org/{relative_url}',
                          cookies=cookies,
                          headers=headers)
  soup = BS(response.text, features='html.parser')
  data = soup.find('script', {'class': 'state-view'}).text
  data = json.loads(data)
  category = data['config']['meta']['breadcrumbs'][2]['category']['seoname']
  name = data['config']['meta']['breadcrumbs'][3]['name']
  if category == 'coffee_shop':
    description = 'Кухня:'
    cuisines = data['stack'][0]['results']['items'][0]['features'][15]['value']
    for i, cuisine in enumerate(cuisines):
      description += str(cuisine['name'])
      description += ', ' if i + 1 != len(cuisines) else ''
  metro_station = data['stack'][0]['results']['items'][0]['metro'][0]['name']
  address = data['stack'][0]['results']['items'][0]['fullAddress']
  coordinates = tuple(data['stack'][0]['results']['items'][0]['geoWhere']
                      ['displayCoordinates'][::-1])
  return Place(category=category,
               name=name,
               description=description,
               metro_station=metro_station,
               address=address,
               coordinates=coordinates)


def main(urls):
  for url in urls:
    place = parse(url)
    models.Place.objects.create(category=place.category,
                                name=place.name,
                                description=place.description,
                                metrostation=place.metro_station,
                                address=place.address,
                                coordinates=str(place.coordinates),
                                url=url)


if __name__ == '__main__':
  df = pandas.read_csv('recomendation/coffee_shop.csv')
  main(df['place'].unique())
