import googlemaps
import json
from GoogleMapsAPIKey import get_my_key

# Define API Key
API_KEY = get_my_key()

# Define Client
gmaps = googlemaps.Client(key=API_KEY)

# Coordinates for Atlanta, GA (correct location)
location = '33.7490,-84.3880'  # Latitude and Longitude for Atlanta, GA

# Define the search parameters
radius = 5000  # Search within a 5km radius
type_place = 'restaurant'  # Search for restaurants

# Perform the search using Places API Nearby Search
places_result = gmaps.places_nearby(location=location, radius=radius, type=type_place)

# List to hold restaurant details
restaurants = []

# Loop through each place in the results to get detailed information
for place in places_result['results']:
    # Get the place ID
    my_place_id = place['place_id']
    
    # Define the fields we want sent back to us, including reviews
    my_fields = ['name', 'formatted_phone_number', 'type', 'rating', 'formatted_address', 'user_ratings_total', 'photo', 'review']

    # Make a request for the details of each restaurant
    place_details = gmaps.place(place_id=my_place_id, fields=my_fields)

    # Append restaurant details to the list
    if 'restaurant' in place_details['result'].get('types', []):
        # Extract the first photo reference if available
        photos = place_details['result'].get('photos', [])
        photo_reference = photos[0]['photo_reference'] if photos else None
        
        # Extract reviews if available
        reviews = place_details['result'].get('reviews', [])

        restaurants.append({
            'name': place_details['result'].get('name'),
            'address': place_details['result'].get('formatted_address'),
            'phone': place_details['result'].get('formatted_phone_number'),
            'rating': place_details['result'].get('rating'),
            'user_ratings_total': place_details['result'].get('user_ratings_total'),
            'types': place_details['result'].get('types'),
            'photo_reference': photo_reference,  # Save the photo reference
            'reviews': reviews  # Save the reviews
        })

# Save the restaurant details to a JSON file
with open('restaurants_data.json', 'w') as outfile:
    json.dump(restaurants, outfile, indent=4)

print("Restaurant data saved to 'restaurants_data.json'")
