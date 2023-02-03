from django.shortcuts import render

import pickle
from joblib import load
model = load('RandomForestRegressor.joblib')

# Create your views here.

def home(request):
    return render(request, "index.html")

def result(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated, lat, longg, sqft_lot15):
    return model.predict(
        [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated, lat, longg, sqft_lot15]]
    )

def predict(request):
    bedrooms = int(request.POST["bedrooms"])
    bathrooms = float(request.POST["bathrooms"])
    sqft_living = int(request.POST["sqft_living"])
    sqft_lot = int(request.POST["sqft_lot"])
    floors = float(request.POST["floors"])
    waterfront = int(request.POST["waterfront"])
    view = int(request.POST["view"])
    condition = int(request.POST["condition"])
    sqft_above = int(request.POST["sqft_above"])
    sqft_basement = int(request.POST["sqft_basement"])
    yr_built = int(request.POST["yr_built"])
    yr_renovated = int(request.POST["yr_renovated"])
    lat = float(request.POST["lat"])
    longg = float(request.POST["long"])
    sqft_lot15 = int(request.POST["sqft_lot15"])   

    pred = result(bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                                waterfront, view, condition, sqft_above,
                                sqft_basement, yr_built, yr_renovated, lat, longg,
                                sqft_lot15)[0]
        
                            
    return render(request, "index.html", {"result":f'house price is {pred}'})