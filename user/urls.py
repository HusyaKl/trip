from calendar import c
from django.urls import path,include                       
from . import views                        

urlpatterns = [
    path('signup/', views.create_user),
    path('signin/', views.sign_in),
    path('current_user/', views.current_user),
    path('get_csrf/', views.csrftoken),
    path('logout/', views.logout),
    path('gitpull/', views.gitpull),
]
   
  