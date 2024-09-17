// Load the restaurant data from the JSON file
fetch('restaurants_data.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const restaurantsList = document.getElementById('restaurants-list');

        if (!data.length) {
            restaurantsList.innerHTML = '<p>No restaurants found.</p>';
            return;
        }

        // Define a type mapping for more user-friendly names
        const typeMapping = {
            "meal_takeaway": "Fast Food",
            "cafe": "Cafe",
            "bar": "Bar",
            "bakery": "Bakery",
            "night_club": "Night Club",
            "lodging": "Hotel",
            "chinese": "Chinese",
            "italian": "Italian",
            "mexican": "Mexican",
            "thai": "Thai",
            "japanese": "Japanese",
            // Add more specific cuisine types as needed
        };

        data.forEach(restaurant => {
            const restaurantCard = document.createElement('div');
            restaurantCard.classList.add('restaurant-card');

            const restaurantInfo = document.createElement('div');
            restaurantInfo.classList.add('restaurant-info');

            // Add photo if available
            if (restaurant.photo_reference) {
                const photoUrl = `https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=${restaurant.photo_reference}&key=AIzaSyAB4mZM4o2Oe4_-ZHmH9gTI3o-gj00pEg4`;
                
                const restaurantImage = document.createElement('img');
                restaurantImage.src = photoUrl;  // Set the photo URL
                restaurantImage.alt = restaurant.name;
                restaurantImage.width = 100;  // Adjust width as needed
                restaurantCard.appendChild(restaurantImage);
            } else {
                // Placeholder for restaurant image (if not available)
                const restaurantImage = document.createElement('img');
                restaurantImage.src = 'https://via.placeholder.com/100'; // Placeholder image
                restaurantCard.appendChild(restaurantImage);
            }

            // Restaurant name
            const restaurantName = document.createElement('h2');
            restaurantName.classList.add('restaurant-name');
            restaurantName.textContent = restaurant.name;
            restaurantInfo.appendChild(restaurantName);

            // Extracting cuisine type from types array and mapping them
            const cuisineTypes = restaurant.types
                .map(type => typeMapping[type] || type)  // Map types to user-friendly names
                .filter(type =>
                    type !== "restaurant" &&  // Exclude generic types
                    type !== "food" &&
                    type !== "point_of_interest" &&
                    type !== "establishment"
                );

            // Display cuisine types if available
            if (cuisineTypes.length > 0) {
                const restaurantTypes = document.createElement('p');
                restaurantTypes.classList.add('restaurant-type');
                restaurantTypes.textContent = cuisineTypes.join(', ');  // Join types by comma
                restaurantInfo.appendChild(restaurantTypes);
            }

            // Restaurant rating
            if (restaurant.rating) {
                const restaurantRating = document.createElement('p');
                restaurantRating.classList.add('restaurant-rating');
                restaurantRating.innerHTML = `⭐ ${restaurant.rating.toFixed(1)} (${restaurant.user_ratings_total} reviews)`;
                restaurantInfo.appendChild(restaurantRating);
            }

            // Restaurant address
            if (restaurant.address) {
                const restaurantAddress = document.createElement('p');
                restaurantAddress.classList.add('restaurant-address');
                restaurantAddress.innerHTML = `<strong>Address:</strong> ${restaurant.address}`;
                restaurantInfo.appendChild(restaurantAddress);
            }

            // Restaurant phone
            if (restaurant.phone) {
                const restaurantPhone = document.createElement('p');
                restaurantPhone.classList.add('restaurant-phone');
                restaurantPhone.innerHTML = `<strong>Phone:</strong> ${restaurant.phone}`;
                restaurantInfo.appendChild(restaurantPhone);
            }

            // Display reviews if available
            if (restaurant.reviews && restaurant.reviews.length > 0) {
                const reviewsTitle = document.createElement('h3');
                reviewsTitle.textContent = 'Reviews:';
                restaurantInfo.appendChild(reviewsTitle);

                restaurant.reviews.slice(0, 3).forEach(review => {  // Limit to first 3 reviews
                    const reviewText = document.createElement('p');
                    reviewText.classList.add('restaurant-review');
                    reviewText.innerHTML = `<strong>${review.author_name}</strong> ⭐ ${review.rating.toFixed(1)}: ${review.text}`;
                    restaurantInfo.appendChild(reviewText);
                });
            }

            restaurantCard.appendChild(restaurantInfo);
            restaurantsList.appendChild(restaurantCard);
        });
    })
    .catch(error => console.error('Error fetching restaurant data:', error));
