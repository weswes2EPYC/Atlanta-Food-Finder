from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def returnHomePage(request):
    return render(request, 'main/home.html', {'isLoggedIn': False})

def restaurants_view(request):
    query = request.GET.get('query', '')
    
    # If no query is provided, return an empty result
    if not query:
        return render(request, 'main/restaurants.html', {'restaurants': [], 'query': query})
    
    # Make the API request to Google Places
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': query,
        'key': settings.GOOGLE_PLACES_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract relevant information from the API response
    restaurants = []
    if 'results' in data:
        for result in data['results']:
            restaurant = {
                'image_url': result.get('photos', [{}])[0].get('photo_reference', ''),
                'name': result.get('name', 'Unknown'),
                'rating': result.get('rating', 'N/A'),
                'reviews': result.get('user_ratings_total', 'N/A'),
                'place_id': result.get('place_id', '')
            }
            restaurants.append(restaurant)

    return render(request, 'main/restaurants.html', {'restaurants': restaurants, 'query': query})