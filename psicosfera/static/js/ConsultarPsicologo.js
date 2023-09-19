function mostrar_contenido() {
    var especialidad = document.getElementById("specialty-input").value;
    $.ajax({
        type: "GET",  // Puedes cambiar el método HTTP según tus necesidades
        url: "filtrar_psicologos/",  
        data: { especialidad: especialidad },
        success: function(data) {
            if(data.length > 0){
                // Supongamos que userContainer es el elemento contenedor con la clase 'divisor-2'
                var userContainer = document.querySelector('#zona-especialista');

                // Limpiar el contenido existente
                userContainer.innerHTML = '';

                // Iterar a través de los datos y agregar las tarjetas al contenedor
                for (var i = 0; i < data.length; i++) {
                    var dataString = JSON.stringify(data[i]);
                    // Eliminar comillas y corchetes
                    dataString = dataString.replace(/[\[\]"]+/g, '');
                    var userParts = dataString.split(",");

                    var userCard = `
                        <div class="card card-small">
                            <div class="card-body profile-card pt-4 d-flex flex-column align-items-center">
                                <img src="../static/img/img-user/profile-img.jpg" alt="Profile" class="rounded-circle">
                                <br>
                                <h2>${userParts[0]}</h2>
                                <h3>${userParts[1]}</h3>
                                <div class="social-links mt-2">
                                    <a href="#" class="twitter"><i class="bi bi-twitter"></i></a>
                                    <a href="#" class="facebook"><i class="bi bi-facebook"></i></a>
                                    <a href="#" class="instagram"><i class="bi bi-instagram"></i></a>
                                    <a href="#" class="linkedin"><i class="bi bi-linkedin"></i></a>
                                </div>
                            </div>
                        </div>
                    `;

                    // Agregar la tarjeta de usuario al contenedor
                    userContainer.innerHTML += userCard;
                }
            }
            else{
                var userContainer = document.querySelector('.contenedor-mapa-contenido');
                // Limpiar el contenido existente
                userContainer.innerHTML = '';
                var userCard = `
                    <div class="titulo-terapia">
                        <h5>No se encontraron coincidencias. Verifica tus datos e intentalo de nuevo.</h5>
                    </div>
                    `;

                    // Agregar la tarjeta de usuario al contenedor
                    userContainer.innerHTML += userCard;
            }

            buscar();
        },
        error: function(xhr, status, error) {
            // Manejar errores aquí
            console.error("Error en la solicitud AJAX:", error);
        }
    });
}