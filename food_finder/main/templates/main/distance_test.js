function getUserLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, handleLocationError);
    } else {
        console.error("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    userLatitude = position.coords.latitude;
    userLongitude = position.coords.longitude;

    console.log(getDrivingDistance(userLatitude, userLongitude, 33.78548139094015, -84.41269927865861))
}

function handleLocationError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            console.error("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            console.error("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            console.error("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            console.error("An unknown error occurred.");
            break;
    }
}

async function getDrivingDistance(originLat, originLng, destinationLat, destinationLng) {
    const apiKey = 'AIzaSyAB4mZM4o2Oe4_-ZHmH9gTI3o-gj00pEg4';
    const serviceUrl = `https://maps.googleapis.com/maps/api/distancematrix/json?origins=${originLat},${originLng}&destinations=${destinationLat},${destinationLng}&mode=driving&units=imperial&key=${apiKey}`;

    try {
        const response = await fetch(serviceUrl);
        const data = await response.json();

        if (data.status === 'OK') {
            const distanceElement = data.rows[0].elements[0];
            if (distanceElement.status === 'OK') {
                const distance = distanceElement.distance.text;
                const duration = distanceElement.duration.text;
                console.log(`Distance: ${distance}, Duration: ${duration}`);
                return { distance, duration };
            } else {
                console.error("No distance available between the points.");
            }
        } else {
            console.error("Error fetching distance data:", data.error_message);
        }
    } catch (error) {
        console.error("Error fetching data from API:", error);
    }
}

getDrivingDistance(44, 44, -30, -30)