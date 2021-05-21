from django.urls import path

from . import views

app_name = 'metro'
urlpatterns = [
    path('', views.index, name='index'),
    path('stations/', views.stations_view, name='stations'),
    path('lignes/', views.lignes_view, name='lignes'),
    path('trajet/', views.trajet_view, name='trajet'),
    path('logout/', views.logout_view, name='logout')
]