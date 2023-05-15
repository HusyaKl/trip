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
from geopy.distance import geodesic
from openrouteservice import Client
import requests
from yandex_geocoder import Client as YaClient

api_key = '5b3ce3597851110001cf62486e78ddcacd9c43fb8852048902ff97a2'
ors_client = Client(key=api_key)

coffee = load(os.path.dirname(os.path.abspath(__file__)) +
             '/savedModel/model.joblib')
rest = load(os.path.dirname(os.path.abspath(__file__)) +
             '/savedModel/rest.joblib')
museum = load(os.path.dirname(os.path.abspath(__file__)) +
             '/savedModel/museum.joblib')
gallery = load(os.path.dirname(os.path.abspath(__file__)) +
             '/savedModel/gallery.joblib')
bar = load(os.path.dirname(os.path.abspath(__file__)) +
             '/savedModel/bar.joblib')

def predict(request):
    user = "Яна"
    coffees = [('Эрна', 3), ('Циники', 2), ('Шоколадница', 4),
                            ('Даблби', 5)]

    my_list = model_predict(coffee, user, coffees)
    print(my_list)
    paginator = Paginator(my_list, 7)
    page_number = request.GET.get('page')
    print('пагинация')
    print(page_number)
    page = paginator.page(page_number)
    print(page.object_list)
    return (HttpResponse(json.dumps(page.object_list)))


def model_predict(model, user, place_likes):
    recomend = model.predict(place_likes, user)
    recomend = recomend.index.tolist()
    a = []
    for i in place_likes:
        a.append(i[0])
    resp = []
    for i in recomend:
        if i not in a:
            resp.append(i)
    my_list = []
    category = ''
    for i in range(len(resp)):
        place = mPlace.objects.filter(name=resp[i])
        addresses = []
        if not place:
            pass
        else:
            for j in range(len(place)):
                category = place[j].category
            if len(place) > 3:
                for j in range(0, 3):
                    addresses.append(place[j].address+' ')
            else:
                for j in range(len(place)):
                    addresses.append(place[j].address+' ')
        my_dict = {'id': i, 'name': resp[i],
                   'address': addresses, 'category': category}
        print(addresses)
        my_list.append(my_dict)
    return (my_list)


@dataclass
class Place:
    category: str
    name: str
    description: str
    metro_station: str
    address: str
    coordinates: tuple
    image: str


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
    category = None
    for i in data['config']['meta']['breadcrumbs']:
        if i.get('type') == 'category':
            category = i['category']['seoname']
            break
    if category is None:
        category = 'None'


    # TODO handle all types of categories
    name = None
    for i in data['config']['meta']['breadcrumbs']:
        if i.get('type') == 'search':
            name = i['name']
            break
    if name is None:
        for i in data['stack'][0]['results']['items']:
            if i['type'] == 'business':
                name = i['title']
    if name is None: name = 'None'
    temp_desscription = data['stack'][0]['results']['items'][0].get('features')
    description = ''
    if temp_desscription:
        for i in temp_desscription:
            if i.get('name') is None: continue
            if i.get('type') == 'bool':
                description += f"{i.get('name').capitalize()}: {str(i.get('value')).replace('True', 'да').replace('False', 'нет')}"
            elif i.get('type') == 'text':
                description += f"{i.get('name').capitalize()}: {i.get('value')}"
            elif i.get('type') == 'enum':
                description += i.get('name').capitalize() + ': '
                values = i.get('value')
                for i, value in enumerate(values):
                    description += value.get('name')
                    description += ', ' if i < (len(values) - 1) else ''
            description += '\n'
    metro_station = data['stack'][0]['results']['items'][0]['metro'][0]['name']
    address = data['stack'][0]['results']['items'][0]['fullAddress']
    coordinates = tuple(data['stack'][0]['results']['items'][0]['geoWhere']
                        ['displayCoordinates'][::-1])
    image = soup.find('div', {'class': 'business-card-view__extend'}).find_all('img')[1]['src']
    return Place(category=category,
                 name=name,
                 description=description,
                 metro_station=metro_station,
                 address=address,
                 coordinates=coordinates,
                 image=image)


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
                                    url=url,
                                    image=place.image)
            bar.next()
        except:
            print('...Skiped')
    bar.finish()


def load_places_from_csv(request):
    filename = request.GET['file']
    if filename:
        df = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+'/'+f'{filename}.csv')
        main(df['place'].unique())
        return HttpResponse('OK: [200]')
    return HttpResponse('Error 403')


@csrf_exempt # TODO remove on release
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
        places.append('restraurant')
    check = request.POST['check5']
    if check == 'true':
        places.append('sight')
    metro_station = request.POST['metro']
    print(metro_station)
    metro = 'Третьяковская'
    u = trip_forming(metro_station, places)
    return HttpResponse(u)

#этот метод отвечает за методику формирования 3 маршрутов на выбор и обращается к trip_forming
def trip_map(metro, places):
    pass
        

#этот метод отвечает за сам алгоритм формирования маршрута
def trip_forming(metro, categories):

    # из request получаем current user(username)
    # из бд получаем список оценок польхователя(следующие строки для теста пока)
    place_reduction_user = [('Волконский', 3), ('Cofix', 2), ('Циники', 4),
                            ('Эрна', 5)]
    user = 'Яна'

    stations = metro_api()
    station = coordinates_of_station(metro, stations)
    print(station)
    x_coordinate = station['lat']
    y_coordinate = station['lng']
    near_stations = near_metrostations(
        stations, station['lat'], station['lng'])
    
    places_in_trip = []
    if (len(categories) == 1) and ('sight' in categories): #человек выбрал что хочет только гулять - маршрут парк и до 6 достопримечательностей
        landmarks = mPlace.objects.filter(category='landmark')
        park = mPlace.objects.filter(category='park')
        places_in_trip.append(places_near_with_metro(landmarks, near_stations, metro, 5))
        places_in_trip.append(places_near_with_metro(park, near_stations, metro, 1))

    elif (len(categories) == 4) and ('sight' not in categories) or (
    len(categories) == 5): #желание посетить все типы мест, каждого не больше 2 чтоб успеть и проверка длины
        number_places = 2
        landmarks = landmarks = mPlace.objects.filter(category='landmark')
        places_in_trip.append(places_near_with_metro(landmarks, near_stations, metro, 2))

    elif (((len(categories) == 1) or (len(categories) == 2) and (
    ('restaurant' in categories) and ('coffee_shop' in categories))) and ('sight' not in categories)) or (
    (len(categories) == 2) and ('sight' in categories)): #один тип места до 3 каждого и 5 дост
        number_places = 3
        landmarks = mPlace.objects.filter(category='landmark')
        places_in_trip.append(places_near_with_metro(landmarks, near_stations, metro, 5, 'landmark'))
        places_in_trip = [sort_overthetop(places_in_trip, station, 5)]
        print('jdchjdcghdcbh')
        print(places_in_trip)

    else: #2 типа мест до 2 и до 3 дост
        number_places = 2
        landmarks = landmarks = mPlace.objects.filter(category='landmark')
        places_in_trip.append(places_near_with_metro(landmarks, near_stations, metro, 3))
  
    if ('restaurant' in categories) and ('coffee_shop' in categories):

        coffees = model_predict(coffee, user, place_reduction_user)
        rests = model_predict(rest, user, place_reduction_user)
        rest_and_coffee = coffees + rests
        places_in_trip.append(places_near_with_metro(rest_and_coffee, near_stations, metro, number_places))
    else:
        if 'restaurant' in categories:
            rests = model_predict(rest, user, place_reduction_user)
            rests = add_places(rests, station)
            places_in_trip.append(places_near_with_metro(rests, near_stations, metro, number_places))

        if 'coffee_shop' in categories:
            coffees = model_predict(coffee, user, place_reduction_user)
            coffees = add_places(coffees, station)
            print(coffees)
            if len(coffees) > number_places:
                c = sort_overthetop([places_near_with_metro(coffees, near_stations, metro, number_places, 'coffee_shop')], station, number_places)
            else:
                c = coffees
            places_in_trip.append(c)

            print('thats ok')
            print(places_in_trip)

        if 'museum' in categories:
            galleries = model_predict(gallery, user, place_reduction_user)
            museums = model_predict(museum, user, place_reduction_user)
            museum_and_gallery = museums + galleries
            places_in_trip.append(places_near_with_metro(museum_and_gallery, near_stations, metro, number_places))

        if 'bar' in categories:
            bars = model_predict(bar, user, place_reduction_user)
            places_in_trip.append(places_near_with_metro(bars, near_stations, metro, number_places))


    if len(places_in_trip) != 0:
        print('kjvkvfjvjbdvhbdvhbhschbvscgvscghvsgvsgvsgv gsv scv hcvh dvhdbh db')
        print(places_in_trip)
        places = sort_places_by_near_metro(places_in_trip, x_coordinate, y_coordinate)  
        print('kjvkvfjvjbdvhbdvhbhschbvscgvscghvsgvsgvsgv gsv scv hcvh dvhdbh db')
        print(places)
        near_places = [[], [], [], []]
        print(len(near_places))
        
        for i in range(len(near_places)):
            near_places[i] = near_all_places(places[i], near_places[i], station)
        print(near_places)
        start_place = []
        for i in range(len(near_places)):
            if near_places[i] != []:
                start_place.append(near_places[i][0][0])

        s_p = []
        for i in range(len(start_place)):
            x, y = split_coordinates(start_place[i].coordinates)
            km = haversine(x, y, station['lat'], station['lng'])
            near_place = (start_place[i], km)
            s_p.append(near_place)
        s_p = sorted(s_p, key=lambda x: x[1])
        start_place = s_p[0]

        
        metro = metro.replace(' ', '+')
        address = f'метро+{metro}/'

        for i in range(len(near_places)):
            if start_place in near_places[i]:
                start = i
        print('start')
        print(start)
        if (start == 0):
            end = 3
        else:
            end = start - 1
        
        for i in range(4):
            if (near_places[end] == []):
                if (end == 0):
                    end = 3
                else:
                    end = end - 1
        
        print('end')
        print(end)
        print(near_places)
        for i in range(len(near_places)):
            if end == i:
                print('poehali')
                print(near_places[i][len(near_places[i])-1][0].address)
                x = split_coordinates(
                    near_places[i][len(near_places[i])-1][0].coordinates)[0]
                y = split_coordinates(
                    near_places[i][len(near_places[i])-1][0].coordinates)[1]

        finish_station = near_metrostations(stations, x, y)[0][0]
        finish_station = coordinates_of_station(finish_station, stations)

        near_places_finish = [[], [], [], []]

       

        for i in range(len(near_places)):
            if end == i:
                near_places_finish[i] = near_finish_places(
                    near_places[i], near_places_finish[i], finish_station)
                
        for i in range(len(near_places)):
            cnt_m = i-1
            cnt_p = i+1
            if start_place in near_places[i]:
                print(i)
                if (i == 0):
                    cnt_m = 3
                elif (i == 3):
                    cnt_p = 0
                    
                near_places[cnt_m] = sorted(
                        near_places[cnt_m], key=lambda x: x[1], reverse=True)
                near_places[cnt_p] = sorted(
                        near_places[cnt_p], key=lambda x: x[1], reverse=True)
                for j in range(i, i+4):
                    if j > 3:
                        j = j%4
                    print(j)
                    if near_places[j] != [] and end != j:
                        address += replace_sth(near_places[j])
                    elif end == j:
                        address += replace_sth(near_places_finish[j])


        finish_station = finish_station['name']
        address += f'метро+{finish_station}/'


        #определение расстояния маршрута
        if start == end:
            dist += near_places_finish[start][0][1]
            dist += check_dist_uno(near_places_finish[start])
        else:
            dist = near_places[start][0][1]
            print(dist)
        i = start 
        iter = [0, 0, 0, 0]
        for j in range(4):
            iter[0] = i
            if i == 0:
                iter[1] = 1
                iter[2] = 2
                iter[3] = 3
            if i == 1:
                iter[1] = 2
                iter[2] = 3
                iter[3] = 0
            if i == 2:
                iter[1] = 3
                iter[2] = 0
                iter[3] = 1
            if i == 3:
                iter[1] = 0
                iter[2] = 1
                iter[3] = 2
        
            if (near_places[iter[1]] != []) and (iter[1] != end) and (iter[0] != end) and ((near_places[iter[0]] != [])):
                dist += check_dist_double(near_places[iter[0]], near_places[iter[1]])
            elif ((near_places[iter[2]] != []) ) and (iter[2] != end) and (iter[1] != end) and (iter[0] != end) and (near_places[iter[1]] == []) and (near_places[iter[0]] != []):
                dist += check_dist_double(near_places[iter[0]], near_places[iter[2]])
            elif (iter[1] == end) and (near_places[iter[0]] != []):
                dist += check_dist_double(near_places[iter[0]], near_places_finish[iter[1]])
                print('oookkk')
            elif (iter[2] == end) and (near_places[iter[0]] != []) and (near_places[iter[1]] == []):
                dist += check_dist_double(near_places[iter[0]], near_places_finish[iter[2]])
            elif (iter[3] == end) and (near_places[iter[0]] != []) and (near_places[iter[1]] == []) and (near_places[iter[2]] == []):
                dist += check_dist_double(near_places[iter[0]], near_places_finish[iter[3]])

            if i == 3:
                i = 0
            else: 
                i = i + 1

        dist += check_dist_uno(near_places_finish[end])
        dist += near_places_finish[end][0][1]


        print('final dist')
        print(dist)
        #разделение на категории
        if dist <= 1.5:
            level = 1
        elif (dist > 1.5 and dist < 3):
            level = 2
        else:
            level = 3

        addresses = address.replace('+', ' ').split('/')
        client = YaClient('4be45663-40b5-41d1-be8d-107b39c200ca')
        for i in range(len(addresses)):
            if addresses[i] == '': continue
            addresses[i] = client.coordinates(addresses[i])
        url_to_maps = f'https://www.google.com/maps/dir/{address}'
        url_to_yamaps = yandex_maps_link_generation(*addresses)
        print(url_to_yamaps)
        print(url_to_maps)

    else:
        url_to_maps = 'null'

    cnt = 0
    response = []
    print(places_in_trip)
    for j in range(len(places_in_trip)):
        for i in places_in_trip[j]:
            print(i)
            my_dict = {'id': cnt, 'name': i.name, 'address': i.address,
                    'category': i.category, 'metro': i.metrostation}
            cnt += 1
            response.append(my_dict)
    response.append(url_to_maps)
    response.append(url_to_yamaps)
    return HttpResponse(json.dumps(response))


# возвращает список станций метро с координатами
def metro_api():
    response = requests.get('https://api.hh.ru/metro/1')
    data = json.loads(response.text)
    c = 0
    array = []
    for i in range(len(data['lines'])):
        for j in range(len(data['lines'][i]['stations'])):
            c = c+1
            my_dict = {'id': c, 'name': data['lines'][i]['stations'][j]['name'], 'lat': data['lines']
                       [i]['stations'][j]['lat'], 'lng': data['lines'][i]['stations'][j]['lng']}
            array.append(my_dict)
    return (array)


# возвращает координаты заданного метро по названию станции
def coordinates_of_station(metro_station, stations):
    for i in range(len(stations)):
        if stations[i]['name'] == metro_station:
            station_X = stations[i]
            return (station_X)


# возвращает массив ближайших станций с расстоянием до них
def near_metrostations(stations, lat, lng):
    near_stations = []
    for i in range(len(stations)):
        km = haversine(stations[i]['lat'], stations[i]['lng'], lat, lng)
        if km < 1.8:
            near_stations.append((stations[i]['name'], km))
    near_stations = sorted(near_stations, key=lambda x: x[1])
    return (near_stations)


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
    # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    r = 6371
    return c * r


def split_coordinates(my_str):
    t = my_str.split('(')
    t = t[1].split(')')
    t = t[0].split(', ')
    coordinates = [float(i) for i in t]
    coordinates = tuple(coordinates)
    return (coordinates)


def replace_sth(places):
    addresses = ''
    print(places)
    for i in places:
        s = i[0].address.replace(' ', '+')
        addresses += s.replace('/', '+')
        addresses += '/'
        print(addresses)
    return (addresses)


def near_finish_places(places, finish_places, finish_station):
    for i in range(len(places)):
        x, y = split_coordinates(places[i][0].coordinates)
        km = haversine(x, y, finish_station['lat'], finish_station['lng'])
        distance = geodesic((x, y), (finish_station['lat'], finish_station['lng'])).km
        print(distance - km)
        if (distance - km) < 0.5:
            near_place = (places[i][0], km)
            finish_places.append(near_place)

    finish_places = sorted(finish_places, key=lambda x: x[1], reverse=True)
    print('finish')
    print(finish_places)
    return (finish_places)


def near_all_places(places, near_places, station):
    for i in range(len(places)):
        x, y = split_coordinates(places[i].coordinates)
        km1 = haversine(x, y, station['lat'], station['lng'])
        km2 = geodesic((x, y), (station['lat'], station['lng'])).km
        print(km1 - km2)
        if (km2- km1) < 0.6:
            near_place = (places[i], km1)
            near_places.append(near_place)
    near_places = sorted(near_places, key=lambda x: x[1])
    print(near_places)
    return (near_places)

def check_dist_uno(places):
    distance = 0
    print(places)
    for i in range(len(places)-1):
        x1, y1 = split_coordinates(places[i][0].coordinates)
        x2, y2 = split_coordinates(places[i+1][0].coordinates)
        km = geodesic((x1, y1), (x2, y2)).km
        coords = [(y1, x1), (y2, x2)]
        r = ors_client.directions(coords, profile='foot-walking', format='geojson', radiuses=1000)
        d = r['features'][0]['properties']['segments'][0]['distance']/1000
        distance += d
        print(distance)
        print('her poimi')
        print(d)     
    return(distance)

def check_dist_double(places1, places2):
    distance = 0
    print(places1)
    for i in range(len(places1)-1):
        x1, y1 = split_coordinates(places1[i][0].coordinates)
        x2, y2 = split_coordinates(places1[i+1][0].coordinates)
        km = geodesic((x1, y1), (x2, y2)).km
        coords = [(y1, x1), (y2, x2)]
        r = ors_client.directions(coords, profile='foot-walking', format='geojson', radiuses=1000)
        d = r['features'][0]['properties']['segments'][0]['distance']/1000
        distance += d
        print(distance)
    x1, y1 = split_coordinates(places1[len(places1)-1][0].coordinates)
    x2, y2 = split_coordinates(places2[0][0].coordinates)
    km = geodesic((x1, y1), (x2, y2)).km
    coords = [(y1, x1), (y2, x2)]
    r = ors_client.directions(coords, profile='foot-walking', format='geojson', radiuses=1000)
    d = r['features'][0]['properties']['segments'][0]['distance']/1000
    distance += d
    print(distance)
    
    return(distance)

def add_places(my_list, station):
    places = []
    for i in range(len(my_list)):
        place = mPlace.objects.filter(name=my_list[i]['name'])
        if not place:
            pass
        else:
            if len(place) > 1:
                near_places = []
                for j in range(len(place)):
                    x, y = split_coordinates(place[j].coordinates)
                    km = haversine(x, y, station['lat'], station['lng'])
                    near_place = (place[j], km)
                    near_places.append(near_place)
                    near_places = sorted(near_places, key=lambda x: x[1])
                places.append(near_places[0][0])
    return(places)

def places_near_with_metro(places, near_stations, metro, number_of_places, categorys):
     # подбор мест с нужной станцией метро или соседними с ней станциями

    places_in_trip = []
    for i in places:
        print('places')
        print(i)
        if i.metrostation == metro:
            places_in_trip.append(i)
    print(places_in_trip)
    if len(places_in_trip) < number_of_places:
        for i in places:
            for j in range(1, len(near_stations)):
                if i.metrostation == near_stations[j][0] and i not in places_in_trip:
                    places_in_trip.append(i)
    if len(places_in_trip) < number_of_places:
        another_places = mPlace.objects.filter(category=categorys)
        for i in another_places:
            if i.metrostation == metro:
                places_in_trip.append(i)
    if len(places_in_trip) < number_of_places:
        for i in another_places:
            for j in range(1, len(near_stations)):
                if i.metrostation == near_stations[j][0]:
                    places_in_trip.append(i)
    return(places_in_trip)

def sort_places_by_near_metro(places_in_trip, x_coordinate, y_coordinate):
    # сортировка мест по возрастанию расстояния до метро
        places = [[], [], [], []]
        print('nhdjdhbjdvbjscbjvdbjdvbhvdnbhevbshcvcegbv ')
        print(places_in_trip)
        for j in range(len(places_in_trip)):
            pl = places_in_trip[j]
            print(pl)
            for i in range(len(pl)):
                x, y = split_coordinates(pl[i].coordinates)
                m1 = x - x_coordinate
                m2 = y - y_coordinate
                print(m1, m2)
                if m1 > 0 and m2 > 0:
                    places[0].append(pl[i])
                elif m1 > 0 and m2 < 0:
                    places[3].append(pl[i])
                elif m1 < 0 and m2 > 0:
                    places[1].append(pl[i])
                elif m1 < 0 and m2 < 0:
                    places[2].append(pl[i])
        return(places)


def yandex_maps_link_generation(*nodes):
    rtext = ''
    for i, node in enumerate(nodes):
        print('node is', node)
        if len(list(node)) != 2: continue
        (long, lat) = node
        long = float(long)
        lat = float(lat)
        if i+1 < len(nodes):
            rtext += f'{lat}%2C{long}~'
        else:
            rtext += f'{lat}%2C{long}'
    result = f'https://yandex.ru/maps/?mode=routes&rtext={rtext}&rtt=pd'
    return result

def sort_overthetop(place, station, count):
    places = []
    place = place[0]
    near_places = []
    for j in range(len(place)):
        x, y = split_coordinates(place[j].coordinates)
        km = haversine(x, y, station['lat'], station['lng'])
        near_place = (place[j], km)
        near_places.append(near_place)
    near_places = sorted(near_places, key=lambda x: x[1])
    for i in range(count):
        places.append(near_places[i][0])
    return(places)
