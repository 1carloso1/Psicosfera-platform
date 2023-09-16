function mostrar_contenido() {
    var especialidad = document.getElementById("specialty-input").value;
    $.ajax({
        type: "GET",  // Puedes cambiar el método HTTP según tus necesidades
        url: "filtrar_psicologos/",  
        data: { especialidad: especialidad },
        success: function(data) {
            // Manejar la respuesta del servidor aquí
            console.log("Input-Text: ", especialidad);
            console.log("Datos recibidos:", data);

            buscar();
        },
        error: function(xhr, status, error) {
            // Manejar errores aquí
            console.error("Error en la solicitud AJAX:", error);
        }
    });
}