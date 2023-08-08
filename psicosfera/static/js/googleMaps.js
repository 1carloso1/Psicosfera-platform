function getLocation() {
    if (navigator.geolocation) {
        const options = {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        };

        navigator.geolocation.getCurrentPosition(
            function(position) {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                const mapElement = document.getElementById('map');

                const apiKey = 'AIzaSyArzco6AwojIFcyWLefRR1MIhArWe0h5q4'; // Reemplaza con tu propia API Key
                const googleMapsScript = document.createElement('script');
                googleMapsScript.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=initMap`;
                document.head.appendChild(googleMapsScript);

                window.initMap = function() {
                    var coord = { lat: latitude, lng: longitude };
                    var map = new google.maps.Map(mapElement, {
                        zoom: 7,
                        center: coord
                    });
                    var marker = new google.maps.Marker({
                        position: coord,
                        map: map
                    });

                    // Cambiar estilo del segundo div para hacerlo visible
                    document.querySelector(".contenedor-mapa").style.display = "flex";
                };
            },
            function(error) {
                alert('No se pudo obtener la ubicación. Verifica la configuración de tu dispositivo.');
            },
            options
        );
    } else {
        alert('Tu navegador no soporta geolocalización.');
    }
}


