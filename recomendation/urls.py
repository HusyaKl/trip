from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  

router = DefaultRouter()


urlpatterns = [
    path('recomendation/', include(router.urls)),
    path('predict/', views.predict)

]