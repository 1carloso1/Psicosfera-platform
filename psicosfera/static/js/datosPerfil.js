$(document).ready(function() {
    // Hacer la solicitud AJAX al cargar la página
    $.ajax({
        url: UrlDatos, 
        type: 'GET',
        dataType: 'json',
        success: function(data) {
          if (data.foto) {
            $('#foto').attr('src', 'data:image/jpeg;base64,' + data.foto);
            $('#foto2').attr('src', 'data:image/jpeg;base64,' + data.foto);
            $('#foto3').attr('src', 'data:image/jpeg;base64,' + data.foto);
          }else{
            $('#foto').hide();
            $('#foto2').hide();
          }
          $('#user').text(data.user);
          $('#user2').text(data.user);
          $('#nombre').text(data.nombre);
          $("#fullName").val(data.nombre);
          $('#especialidad').text(data.especialidad);
          $('#especialidad2').text(data.especialidad);
          $('#descripcion').text(data.descripcion);
          $('#descripcion2').text(data.descripcion);
          $('#especiality').val(data.especialidad);
          $('#direccion').text(data.direccion);
          $('#address').val(data.direccion);
          $('#edad').text(data.edad);
          $('#age').val(data.edad);
          $('#correo').text(data.correo);
          $("#Email").val(data.correo);
          $('#numero').text(data.telefono);
          $("#Phone").val(data.telefono);
          
          if(data.psicologo == 1){
            $('#facebook').attr('href', data.facebook);
            $("#Facebook").val(data.facebook);
            $('#instagram').attr('href', data.instagram);
            $("#Instagram").val(data.instagram);
            $('#linkedin').attr('href', data.linkedin);
            $("#Linkedin").val(data.linkedin);
            $('#twitter').attr('href', data.twitter);
            $("#Twitter").val(data.twitter);
            $('#user').attr('data', 1);
            console.log($('#user').attr('data'))
          }else{
            $('#facebook').hide();
            $("#Facebook").hide();
            $('#instagram').hide();
            $("#Instagram").hide();
            $('#linkedin').hide();
            $("#Linkedin").hide();
            $('#twitter').hide();
            $("#Twitter").hide();
            $(".hide").hide();
          }
        },
        error: function(error) {
            console.log(error);
        }
    });
});