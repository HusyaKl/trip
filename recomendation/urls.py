from django.urls import path, include
from . import views  


urlpatterns = [
    path('predict/', views.predict),
    path('load_places_from_csv/', views.load_places_from_csv),
    path('analise/', views.analise),

]