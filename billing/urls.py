from django.urls import path

from . import views

app_name = 'billing'

urlpatterns = [
    path('plantfinder', views.plantfinder,name='plantfinder'),
    path('localna',views.localna,name='localna'),
    path('plantlist',views.plantlist,name='plantlist'),
    path('lplantfinder', views.lplantfinder,name='lplantfinder'),
    path('lplantlist',views.lplantlist,name='lplantlist'),
    path('local',views.local,name='local'),
    path('localava',views.localava,name='localava'),
]
