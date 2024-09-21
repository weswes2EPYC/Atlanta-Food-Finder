from django.shortcuts import render
import requests
from django.conf import settings

def returnHomePage(request):
    return render(request, 'main/home.html', {'isLoggedIn': False})

def restaurants_view(request):
    query = request.GET.get('query', '')
    min_rating = request.GET.get('rating', 0)

    if not query:
        return render(request, 'main/restaurants.html', {'restaurants': [], 'query': query, 'selected_rating': min_rating})

    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': query,
        'type': 'restaurant',
        'key': settings.GOOGLE_PLACES_API_KEY
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

                restaurant = {
                    'image_url': image_url,
                    'name': result.get('name', 'Unknown'),
                    'rating': rating,
                    'reviews': result.get('user_ratings_total', 'N/A'),
                    'place_id': result.get('place_id', '')
                }
                restaurants.append(restaurant)

    return render(request, 'main/restaurants.html', {'restaurants': restaurants, 'query': query, 'selected_rating': min_rating})
