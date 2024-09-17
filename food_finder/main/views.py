from django.shortcuts import render

# Create your views here.
def returnHomePage(request):
    return render(request, 'main/home.html', {'isLoggedIn': False})

def restaurantDetailsPage(request, restaurant_id):
    print(restaurant_id)
    return render(request, 'main/details.html', {
        "name": "Lucky Buddha",
        "image_url": "https://cdn.usarestaurants.info/assets/uploads/3bdbe73b33fa800fc27e545c68ade271_-united-states-georgia-fulton-county-atlanta-lucky-buddha-404-885-1518htm.jpg",
        "num_reviews": "201",
        "rating": "4.2",
        "genre": "Chinese, Fast Food",
        "address": "529 10th St NW, Atlanta, GA 30318",
        "distance": "1.1 mi",
        "phone": "(404)-249-9883",
        "reviews": [
            {
                "author": "John Doe",
                "rating": "4.2",
                "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            },
            {
                "author": "Jane Doe",
                "rating": "3.6",
                "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            }
        ]
    })