from types import MethodDescriptorType
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from matplotlib.pyplot import title
import requests
from math import radians, cos, sin, asin, sqrt
import json
from joblib import load
import os
from .savedModel.coffeemodel import CoffeeshopsRecomendation
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup as BS
from dataclasses import dataclass
import pandas
from django.views.decorators.csrf import csrf_exempt
from recomendation.models import Place as mPlace
from progress.bar import Bar

model = load(os.path.dirname(os.path.abspath(__file__))+'/savedModel/model.joblib')

def predict(request):
    user = "Яна"
    place_reduction_user = [('Эрна', 3), ('Циники', 2), ('Шоколадница', 4), 
                         ('Даблби', 5)]
    my_list = model_predict(user, place_reduction_user)
    paginator = Paginator(my_list, 7)
    page_number = request.GET.get('page')
    print('пагинация')
    print(page_number)
    page = paginator.page(page_number)
    print(page.object_list)
    return(HttpResponse(json.dumps(page.object_list)))

def model_predict(user, place_likes):
    recomend = model.predict(place_likes, user)
    recomend = recomend.index.tolist()
    a=[]
    for i in place_likes:
        a.append(i[0])
    resp = []
    for i in recomend:
        if i not in a:
            resp.append(i)
    my_list = []
    for i in range(0, len(resp), 1):
        my_dict = {'id': i, 'title': resp[i] }
        my_list.append(my_dict)
    return(my_list)

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
      'maps_routes_travel_mode': 'masstransit',
      '_ym_d': '1670147721',
      'tmr_lvid': '91937e083617052a09d5b73da33aba62',
      'tmr_lvidTS': '1670240683142',
      'i': 'S6qDcBpMZxxJh8qVUHBHKbHZmeKzPHcEM/QAHfPYetwglmsAZ8LCvGYJpKuWGm6f5nlPO93rEwyr+F8NBwRpH2sU4gc=',
      'L': 'e1BJRFoJX3B3XGldT3RZSF18UnBaXU56LCgbHyInJQ==.1672528653.15208.361071.d6f8882e4456185f38a3bb9158a0f98a',
      'yandex_login': 'arklual',
      'yashr': '9919303011674047544',
      'cycada': 'I1J9/BrF4fSvFUfLc0g+4vcNhiWPHtw2YcnuHQqC1hU=',
      'sae': '0:8c5b9e54-9e52-4d6f-83a4-a3c0450C13C0:p:22.11.3.838:l:d:RU:20220516',
      'is_gdpr': '0',
      'is_gdpr_b': 'CMjpUhDbogEoAg==',
      'yabs-frequency': '/5/0G00020Zn6C00000/yTwHdct3rboCIY6gLHYeSrvqPunA8O6f6ZyhvZvRZ4f0lmdSQgKlb5ICIa00/',
      'ys': 'svt.1#def_bro.1#wprid.1674589834631939-15007422606880292127-sas2-0821-sas-l7-balancer-8080-BAL-4037#ybzcc.ru#newsca.native_cache',
      'yp': '1674644544.uc.ru#1674644544.duc.ru#1705126405.cld.2574584#1989949835.pcs.0#1689734035.szm.1:1920x1080:1872x948#1677267162.csc.1#1674830628.mcv.0#1674678601.nwcst.1674593400_16_2',
      '_yasc': 'v9JUK/rD+tacvRtmHRr0yeZ2dk7LVQ31ppqyxwMJmgTasQiuKnxxxJToFUN3ISTO3IK95frbWA3ziw==',
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
  temp_desscription = data['stack'][0]['results']['items'][0]['features']
  description = ''
  '''
  for i in temp_desscription:
    if i.get('name') is not None:
      description += i.get('name') + ': '
      if isinstance(i['value'], list):
        for j, value in enumerate(i['value']):
          description += str(value)
          description += ', ' if j != len(i)-1 else ''
        else:
          value = str(value).replace('True', 'Да')
          value = str(value).replace('False', 'Нет')
          description += value
  '''
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
    bar = Bar('Loading csv to db.', max=len(urls))
    for url in urls:
      try:
        place = parse(url)
        mPlace.objects.create(category=place.category,
                                    name=place.name,
                                    description=place.description,
                                    metrostation=place.metro_station,
                                    address=place.address,
                                    coordinates=str(place.coordinates),
                                    url=url)
        bar.next()
      except:
        print('...Skiped')
    bar.finish()

def load_places_from_csv(request):
    df = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+'/coffee_shops.csv')
    main(df['place'].unique())
    return HttpResponse('OK: [200]')

@csrf_exempt
def analise(request):
    places = []
    check = request.POST['check1']
    if check == 'true':
      places.append('coffee_shop')
    check = request.POST['check2']
    if check == 'true':
      places.append('museum')
    check = request.POST['check3']
    if check == 'true':
      places.append('bar')
    check = request.POST['check4']
    if check == 'true':
      places.append('restraunt')
    check = request.POST['check5']
    if check == 'true':
      places.append('sight')
    metro_station = request.POST['metro']
    print
    u = trip_forming(metro_station)
    return HttpResponse(u)

#возвращает список станций метро с координатами
def metro_api():
  response = requests.get('https://api.hh.ru/metro/1')
  data = json.loads(response.text)
  c=0
  array = []
  for i in range(len(data['lines'])):
    for j in range(len(data['lines'][i]['stations'])):
      c = c+1
      my_dict = {'id': c, 'name': data['lines'][i]['stations'][j]['name'],'lat':data['lines'][i]['stations'][j]['lat'], 'lng': data['lines'][i]['stations'][j]['lng']}
      array.append(my_dict)
  return(array)
  
#возвращает координаты заданного метро по названию станции
def coordinates_of_station(metro_station, stations):
  for i in range(len(stations)):
      if stations[i]['name'] == metro_station:
        station_X = stations[i]
        return(station_X)

#возвращает массив ближайших станций с расстоянием до них
def near_metrostations(stations, lat, lng):
  near_stations = []
  for i in range(len(stations)):
    km = haversine(stations[i]['lat'], stations[i]['lng'], lat, lng)
    if km < 1.8:
      near_stations.append((stations[i]['name'], km))
  near_stations = sorted(near_stations, key=lambda x: x[1])
  return(near_stations)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def trip_forming(metro):
    # из request получаем current user(username) 
    # из бд получаем список оценок польхователя(следующие строки для теста пока)
    place_reduction_user = [('Волконский', 3), ('Cofix', 2), ('Циники', 4), 
                         ('Эрна', 5)]
    user = 'Яна'
    my_list = model_predict(user, place_reduction_user)
    stations = metro_api()
    station = coordinates_of_station(metro, stations)
    print(station)
    x_coordinate = station['lat']
    y_coordinate = station['lng']
    near_stations = near_metrostations(stations, station['lat'], station['lng'])
    places = []
    for i in range(len(my_list)):
      place = mPlace.objects.filter(name=my_list[i]['title'])
      if not place:
        pass
      else:
        if len(place)> 1:
          near_places = []
          for j in range(len(place)):
            x, y = split_coordinates(place[j].coordinates)
            km = haversine(x, y, station['lat'], station['lng'])
            near_place = (place[j], km)
            near_places.append(near_place)
            near_places = sorted(near_places, key=lambda x: x[1])
          places.append(near_places[0][0])
          print(places)

    #подбор мест с нужной станцией метро или соседними с ней станциями

    places_in_trip = []
    for i in places:
      if i.metrostation == metro:
        places_in_trip.append(i)
    if len(places_in_trip)<2:
      for i in places:
        for j in near_stations:
          if i.metrostation == j[0]:
            places_in_trip.append(i)
    if len(places_in_trip)<2:
      another_places = mPlace.objects.all()
      for i in another_places:
        if i.metrostation == metro:
          places_in_trip.append(i)
    if len(places_in_trip)<2:
      for i in another_places:
        for j in near_stations:
          if i.metrostation == j[0]:
            places_in_trip.append(i)
    if len(places_in_trip)!=0:
      print(places_in_trip)
      #сортировка мест по возрастанию расстояния до метро
      places_1 = []
      places_2 = []
      places_3 = []
      places_4 = []
      for i in range(len(places_in_trip)):
        x, y = split_coordinates(places_in_trip[i].coordinates)
        m1 = x - x_coordinate
        m2 = y - y_coordinate
        if m1>0 and m2>0:
          places_1.append(places_in_trip[i])
        elif m1>0 and m2<0:
          places_4.append(places_in_trip[i])
        elif m1<0 and m2>0:
          places_2.append(places_in_trip[i])
        elif m1<0 and m2<0:
          places_3.append(places_in_trip[i])

      near_places_1 = []
      near_places_2 = []
      near_places_3 = []
      near_places_4 = []
      for i in range(len(places_1)):
        x, y = split_coordinates(places_1[i].coordinates)
        km = haversine(x, y, station['lat'], station['lng'])
        near_place = (places_1[i], km)
        near_places_1.append(near_place)

      for i in range(len(places_2)):
        x, y = split_coordinates(places_2[i].coordinates)
        km = haversine(x, y, station['lat'], station['lng'])
        near_place = (places_2[i], km)
        near_places_2.append(near_place)

      for i in range(len(places_3)):
        x, y = split_coordinates(places_3[i].coordinates)
        km = haversine(x, y, station['lat'], station['lng'])
        near_place = (places_3[i], km)
        near_places_3.append(near_place)

      for i in range(len(places_4)):
        x, y = split_coordinates(places_4[i].coordinates)
        km = haversine(x, y, station['lat'], station['lng'])
        near_place = (places_4[i], km)
        near_places_4.append(near_place)
      
      near_places_1 = sorted(near_places_1, key=lambda x: x[1])
      near_places_2 = sorted(near_places_2, key=lambda x: x[1])
      near_places_3 = sorted(near_places_3, key=lambda x: x[1])
      near_places_4 = sorted(near_places_4, key=lambda x: x[1])
      start_place = []
      if near_places_1 != []:
        start_place.append(near_places_1[0][0])
      if near_places_2 != []:
        start_place.append(near_places_2[0][0])
      if near_places_3 != []:
        start_place.append(near_places_3[0][0])
      if near_places_4 != []:
        start_place.append(near_places_4[0][0])
      s_p = []
      for i in range(len(start_place)):
        x, y = split_coordinates(start_place[i].coordinates)
        km = haversine(x, y, station['lat'], station['lng'])
        near_place = (start_place[i], km)
        s_p.append(near_place)
      s_p = sorted(s_p, key=lambda x: x[1])
      start_place = s_p[0]
      address = f'метро+{metro}/'
      if start_place in near_places_1:
        near_places_2 = sorted(near_places_2, key=lambda x: x[1], reverse=True)
        near_places_4 = sorted(near_places_4, key=lambda x: x[1], reverse=True)
        if near_places_1 != []:
          end = 1
          for i in near_places_1:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_2 != []:
          end = 2
          for i in near_places_2:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_3 != []:
          end = 3
          for i in near_places_3:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_4 != []:
          end = 4
          for i in near_places_4:
            address += i[0].address.replace(' ', '+')
            address += '/'
      if start_place in near_places_2:
        near_places_3 = sorted(near_places_3, key=lambda x: x[1], reverse=True)
        near_places_1 = sorted(near_places_1, key=lambda x: x[1], reverse=True)
        if near_places_2 != []:
          end = 2
          for i in near_places_2:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_3 != []:
          end = 3
          for i in near_places_3:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_4 != []:
          end = 4
          for i in near_places_4:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_1 != []:
          end = 1
          for i in near_places_1:
            address += i[0].address.replace(' ', '+')
            address += '/'
      if start_place in near_places_3:
        near_places_4 = sorted(near_places_4, key=lambda x: x[1], reverse=True)
        near_places_2 = sorted(near_places_2, key=lambda x: x[1], reverse=True)
        if near_places_3 != []:
          end = 3
          for i in near_places_3:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_4 != []:
          end = 4
          for i in near_places_4:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_1 != []:
          end = 1
          for i in near_places_1:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_2 != []:
          end = 2
          for i in near_places_2:
            address += i[0].address.replace(' ', '+')
            address += '/'
      if start_place in near_places_4:
        near_places_1 = sorted(near_places_1, key=lambda x: x[1], reverse=True)
        near_places_3 = sorted(near_places_3, key=lambda x: x[1], reverse=True)
        if near_places_4 != []:
          end = 4
          for i in near_places_4:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_1 != []:
          end = 1
          for i in near_places_1:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_2 != []:
          end = 2
          for i in near_places_2:
            address += i[0].address.replace(' ', '+')
            address += '/'
        if near_places_3 != []:
          end = 3
          for i in near_places_3:
            address += i[0].address.replace(' ', '+')
            address += '/'
  
      if end==1:
        x = split_coordinates(near_places_1[len(near_places_1)-1][0].coordinates)[0]
        y = split_coordinates(near_places_1[len(near_places_1)-1][0].coordinates)[1]
      if end==2:
        x = split_coordinates(near_places_2[len(near_places_2)-1][0].coordinates)[0]
        y = split_coordinates(near_places_2[len(near_places_2)-1][0].coordinates)[1]
      if end==3:
        x = split_coordinates(near_places_3[len(near_places_3)-1][0].coordinates)[0]
        y = split_coordinates(near_places_3[len(near_places_3)-1][0].coordinates)[1]
      if end==4:
        x = split_coordinates(near_places_4[len(near_places_4)-1][0].coordinates)[0]
        y = split_coordinates(near_places_4[len(near_places_4)-1][0].coordinates)[1]
      
      finish_station = near_metrostations(stations, x, y)[0][0]
      address += f'метро+{finish_station}/'  
      
      url_to_maps = f'https://www.google.com/maps/dir/{address}'

      print(url_to_maps)
      
    else: 
      url_to_maps = 'null'
    return(url_to_maps) 

def split_coordinates(my_str):
    t = my_str.split('(')
    t = t[1].split(')')
    t = t[0].split(', ')
    coordinates = [float(i) for i in t]
    coordinates = tuple(coordinates)
    return(coordinates)



