from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SavedRestaurants, save_restaurant, get_saved_restaurants, unsave_restaurant, is_restaurant_saved
import googlemaps
import http
import json

# this is temporary, change this to .env later
API_KEY = "AIzaSyAB4mZM4o2Oe4_-ZHmH9gTI3o-gj00pEg4"

# Create your views here.
def returnHomePage(request):
    return render(request, 'main/home.html', {'isLoggedIn': False})

def restaurantDetailsPage(request, restaurant_id):
    try:
        restaurant_id = "ChIJgUolJWwE9YgRnxg5IduXOsg"
        gmaps = googlemaps.Client(key=API_KEY)
        res = gmaps.place(restaurant_id)["result"]
        if "restaurant" not in res["types"]:
            return redirect("/") # redirect if not a restaurant

        is_saved = False
        if request.user.is_authenticated:
            print(request.user.username)
            is_saved = is_restaurant_saved(request.user.username, restaurant_id)
            print("fail")

        try:
            photo = res["photos"][0]["photo_reference"]
        except:
            photo = "https://icons.veryicon.com/png/o/business/new-vision-2/picture-loading-failed-1.png"
        return render(request, 'main/details.html', {
            "name": res["name"],
            "image_url": f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={photo}&key={API_KEY}",
            "num_reviews": res['user_ratings_total'],
            "rating": res["rating"],
            "address": res["formatted_address"],
            "phone": res["formatted_phone_number"],
            "reviews": res["reviews"],
            "map": f"https://www.google.com/maps/embed/v1/place?key={API_KEY}&q=place_id:{restaurant_id}",
            "is_saved": is_saved,
            "id": restaurant_id
        })
    except:
        return redirect("/") # if restaurant don't exist, redirect to home page
    
def saveRestaurant(request, restaurant_id):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({
            "success": False
        }), status=400)
    if request.user.is_authenticated:
        is_saved = is_restaurant_saved(request.user.username, restaurant_id)
        if is_saved:
            unsave_restaurant(request.user.username, restaurant_id)
            return HttpResponse(json.dumps({
                "success": True,
                "is_saved": False
            }), status=200) 
        else:
            save_restaurant(request.user, restaurant_id)
            return HttpResponse(json.dumps({
                "success": True,
                "is_saved": True
            }), status=200) 