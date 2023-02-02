from calendar import c
from django.urls import path,include               
from rest_framework import routers            
from . import views                        

router = routers.DefaultRouter()                   
router.register(r'accounts', views.AccountView, 'accounts')  

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.create_user),
    path('signin/', views.sign_in),
    path('current_user/', views.current_user),
    path('get_csrf/', views.csrftoken),
]
   
  