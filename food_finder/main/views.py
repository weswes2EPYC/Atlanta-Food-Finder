from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

def returnHomePage(request):
    return render(request, 'main/home.html', {'isLoggedIn': False})

def restaurants_view(request):
    query = request.GET.get('query', '')
    min_rating = request.GET.get('rating', 0)
    max_distance = float(request.GET.get('distance', 9999))
    user_latitude = request.GET.get('user_latitude')
    user_longitude = request.GET.get('user_longitude')
    radius_miles = 10
    radius_km = radius_miles * 1.60934

    # Load the page if query is present
    if not query:
        return render(request, 'main/restaurants.html', {'restaurants': [], 'query': 'restaurants', 'selected_rating': min_rating})

    # API call logic
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': query,
        'type': 'restaurant',
        'key': settings.GOOGLE_PLACES_API_KEY,
        'radius': radius_km * 50000
    }

    response = requests.get(url, params=params)
    data = response.json()

    restaurants = []
    if 'results' in data:
        for result in data['results']:
            rating = result.get('rating', 0)
            if float(rating) >= float(min_rating):
                photo_reference = result.get('photos', [{}])[0].get('photo_reference', '')
                if photo_reference:
                    image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=300&photoreference={photo_reference}&key={settings.GOOGLE_PLACES_API_KEY}"
                else:
                    image_url = '/path/to/default/image.jpg'

                latitude = result['geometry']['location']['lat']
                longitude = result['geometry']['location']['lng']

                if user_latitude and user_longitude:
                    distance = get_driving_distance(user_latitude, user_longitude, latitude, longitude)
                    parsed_distance = parse_distance(distance)
                else:
                    distance = 'Loading...'
                    parsed_distance = 9999

                if parsed_distance <= float(max_distance) or float(max_distance) == 9999:
                    restaurant = {
                        'image_url': image_url,
                        'name': result.get('name', 'Unknown'),
                        'rating': rating,
                        'reviews': result.get('user_ratings_total', 'N/A'),
                        'place_id': result.get('place_id', ''),
                        'latitude': latitude,
                        'longitude': longitude,
                        'distance': distance
                    }
                    restaurants.append(restaurant)

    return render(request, 'main/restaurants.html', {'restaurants': restaurants, 'query': query, 'selected_rating': min_rating})

def get_driving_distance(origin_lat, origin_lng, dest_lat, dest_lng):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    params = {
        'origins': f'{origin_lat},{origin_lng}',
        'destinations': f'{dest_lat},{dest_lng}',
        'mode': 'driving',
        'units': 'imperial',
        'key': settings.GOOGLE_PLACES_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'OK' and data['rows']:
        distance_element = data['rows'][0]['elements'][0]
        if distance_element['status'] == 'OK':
            return distance_element['distance']['text']
    return 'N/A'

def parse_distance(distance):
    if 'mi' in distance:
        return float(distance.split()[0])
    elif 'ft' in distance:
        return float(distance.split()[0]) / 5280
    else:
        return 9999