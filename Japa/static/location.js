window.onload = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${position.coords.latitude}&lon=${position.coords.longitude}`)
        .then(response => response.json())
        .then(data => {
            let road = data.address.road;
            let postalCode = data.address.postcode;
            let city = data.address.city;
            document.getElementById("location").innerHTML = `${road}, ${postalCode}, ${city}`;
        })
        .catch(error => console.error(error));
}