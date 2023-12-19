$(document).ready(function() {
    // Hacer la solicitud AJAX al cargar la página
    $.ajax({
        url: 'datos/', 
        type: 'POST',
        dataType: 'json',
        success: function(data) {
        console.log("Success");
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
          $('#certificado').attr('src', 'data:application/pdf;base64,' + data.certificado);
          $('#curriculum').attr('src', 'data:application/pdf;base64,' + data.curriculum);
          $('#user').text(data.user);
          $('#user2').text(data.user);
          $('#nombre').text(data.nombre);
          $("#fullName").val(data.nombre);
          $('#especialidad').text(data.especialidad);
          $('#especialidad2').text(data.especialidad);
          $('#institucion').text(data.institucion);
          $('#institucion2').val(data.institucion);
          $('#cedula').text(data.cedula);
          
          $('#descripcion').text(data.descripcion);
          $('#descripcion2').text(data.descripcion);
          $('#especiality').val(data.especialidad);
          
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
          if(data.cons_registrado == 1){
            $('#direccion').text(data.direccion);
            direccion = data.direccion;
            $('#address').val(data.direccion);
            $('#cierre').text(data.cierre);
            $('#apertura').text(data.apertura);
            $('#cierre2').val(data.cierre);
            $('#apertura2').val(data.apertura);
            $('#horario').text(data.apertura + ' - ' + data.cierre);
          }
          else{
            $('#direccion').hide();
            $('#address').hide();
            $('#cierre').hide();
            $('#apertura').hide();
            $('#horario').hide();
          }

        }
        },
        error: function(error) {
            console.log(error);
        }
    });
});