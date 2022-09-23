from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import joblib

import pandas as pd

model = joblib.load('predict_app/ml_models/meta_ODC_FIFA2022.odc')

# Create your views here.

fifa_ranking = pd.read_csv('predict_app/data/fifa_ranking.csv')
countries = fifa_ranking['country_full'].unique()


def index(request):
    context = {
        'countries_list': sorted(countries),
    }
    return render(request, 'predict_app/index.html', context)


def predict(request):
    home_county = request.POST['home_county']
    away_county = request.POST['away_county']

    winner_country = away_county
    print(winner_country)

    return HttpResponseRedirect(reverse('predict_app:results', args=(home_county, away_county, winner_country,)))


def results(request, home_county, away_county, winner_country):
    context = {
        'countries_list': sorted(countries),
        'home_county': home_county,
        'away_county': away_county,
        'winner_country': winner_country,
    }
    return render(request, 'predict_app/result.html', context)
