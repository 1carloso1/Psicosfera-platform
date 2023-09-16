// Variable para almacenar las coordenadas
var coordenadas = {};

function buscar() {
    var specialty = document.getElementById("specialty-input").value;
    var location = document.getElementById("location-input").value;
    const mapElement = document.getElementById('map');

    // Utiliza la API de Google Maps Geocoding para obtener las coordenadas de la ubicación
    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({ 'address': location }, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            var lat = results[0].geometry.location.lat();
            var lng = results[0].geometry.location.lng();

            // Almacena las coordenadas en la variable coordenadas
            coord = { lat: lat, lng: lng };

            console.log('Coordenadas:', coord.lat, coord.lng);

            var map = new google.maps.Map(mapElement, {
                zoom: 13,
                center: coord
            });
            var marker = new google.maps.Marker({
                position: coord,
                map: map
            });

            // Cambiar estilo del segundo div para hacerlo visible
            document.querySelector(".contenedor-mapa").style.display = "flex";

        
        
        } else {
            // Maneja el error de geocodificación aquí
            alert('Ingrese una ubicación correcta.');
        }
    });
}

    // Ahora puedes utilizar las coordenadas en tu página web según tus necesidades
            //