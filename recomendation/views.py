from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from joblib import load
import os
from .savedModel.coffeemodel import CoffeeshopsRecomendation
from django.core.paginator import Paginator
model = load(os.path.dirname(os.path.abspath(__file__))+'/savedModel/model.joblib')

def predict(request):
    user = "Яна"
    place_reduction_user = [('Эрна', 3), ('Циники', 2), ('Шоколадница', 4), 
                         ('Даблби', 5)]
    recomend = model.predict(place_reduction_user, user)
    recomend = recomend.index.tolist()
    a=[]
    for i in place_reduction_user:
        a.append(i[0])
    resp = []
    for i in recomend:
        if i not in a:
            resp.append(i)
    my_list = []
    for i in range(0, len(resp), 1):
        my_dict = {'id': i, 'title': resp[i] }
        my_list.append(my_dict)
    paginator = Paginator(my_list, 7)
    page_number = request.GET.get('page')
    print('пагинация')
    print(page_number)
    page = paginator.page(page_number)
    print(page.object_list)
    return(HttpResponse(json.dumps(page.object_list)))

 
