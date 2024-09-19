from django.shortcuts import render, redirect
import googlemaps
import json

# this is temporary, change this to .env later
API_KEY = "" # add your own api key

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
        print("hi")
        try:
            photo = res["photos"][0]["photo_reference"]
        except:
            photo = "https://icons.veryicon.com/png/o/business/new-vision-2/picture-loading-failed-1.png"
        print("hi2")
        return render(request, 'main/details.html', {
            "name": res["name"],
            "image_url": f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={photo}&key={API_KEY}",
            "num_reviews": res['user_ratings_total'],
            "rating": res["rating"],
            "address": res["formatted_address"],
            "phone": res["formatted_phone_number"],
            "reviews": res["reviews"],
            "map": f"https://www.google.com/maps/embed/v1/place?key={API_KEY}&q=place_id:{restaurant_id}"
        })
    except:
        return redirect("/") # if restaurant don't exist, redirect to home page
    



    