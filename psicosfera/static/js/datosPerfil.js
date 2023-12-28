$(document).ready(function() {
    // Hacer la solicitud AJAX al cargar la página
  $.ajax({
      url: UrlDatos, 
      type: 'GET',
      dataType: 'json',
      success: function(data) {
      if (data.usuario == "default"){
        $('#foto3').attr('src', UrlImagenDefault);
      }

      if (data.usuario == "registrado"){
        if (data.foto) {
          $('#foto').attr('src', 'data:image/jpeg;base64,' + data.foto);
          $('#foto2').attr('src', 'data:image/jpeg;base64,' + data.foto);
          $('#foto3').attr('src', 'data:image/jpeg;base64,' + data.foto);
        }else{
          $('#foto').hide();
          $('#foto2').hide();
          $('#foto3').hide();
        }
        $('#user2').text(data.user);
        $('#user').text(data.user);
        $('#userName').val(data.user);
        $('#nombre').text(data.nombre +' '+ data.apellidos);
        $("#firstName").val(data.nombre);
        $("#lastName").val(data.apellidos);
        $('#edad').text(data.edad);
        $('#age').val(data.edad);
        $('#correo').text(data.correo);
        $("#Email").val(data.correo);
        $('#numero').text(data.telefono);
        $("#Phone").val(data.telefono);
        $('#descripcion').text(data.descripcion);
        $('#descripcion2').text(data.descripcion);

        if (data.psicologo == 1){
          $('#especialidad').text(data.especialidad);
          $('#especialidad2').text(data.especialidad);
          $('#institucion').text(data.institucion);
          $('#certificado').attr('src', 'data:application/pdf;base64,' + data.certificado);
          $('#curriculum').attr('src', 'data:application/pdf;base64,' + data.curriculum);
          $('#institucion2').val(data.institucion);
          $('#cedula').text(data.cedula);
          
         
          $('#especiality').val(data.especialidad);
          
          $('#facebook').attr('href', data.facebook);
          $("#Facebook").val(data.facebook);
          $('#instagram').attr('href', data.instagram);
          $("#Instagram").val(data.instagram);
          $('#linkedin').attr('href', data.linkedin);
          $("#Linkedin").val(data.linkedin);
          $('#twitter').attr('href', data.twitter);
          $("#Twitter").val(data.twitter);


          $('#direccion').text(data.direccion);
          $('#address').val(data.direccion);
          $('#cierre').text(data.cierre);
          $('#apertura').text(data.apertura);
          $('#cierre2').val(data.cierre);
          $('#apertura2').val(data.apertura);
          $('#horario').text(data.apertura + ' - ' + data.cierre);

        }
      }
    },
    error: function(error) {
      console.log(error);
    }
  });
});