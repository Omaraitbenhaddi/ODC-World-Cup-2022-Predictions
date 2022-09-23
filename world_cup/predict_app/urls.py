from django.urls import path

from . import views

app_name = 'predict_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict', views.predict, name='predict'),
    path('<str:home_county>/<str:away_county>/<str:winner_country>/results/',
         views.results, name='results'),
]
