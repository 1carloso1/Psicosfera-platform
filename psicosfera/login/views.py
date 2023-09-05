from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *

from django.views.generic import TemplateView

from django.contrib.auth.models import User, Group, Permission
from psicologo.models import Psicologo
from paciente.models import Paciente
from psicologo.forms import FormPsicologo
from paciente.forms import FormPaciente
from django.db.models.signals import post_save


# @login_required
# def agregar_paciente(request):
#     if not request.user.groups.filter(name='Pacientes').exists():
#         paciente_group = Group.objects.get(name='Pacientes')
#         request.user.groups.add(paciente_group)
#     return redirect('nuevo_paciente')  

# @login_required
# def agregar_psicologo(request):
#     print(request)
#     if not request.user.groups.filter(name='Psicologos').exists():
#         psicologo_group = Group.objects.get(name='Psicologos')
#         request.user.groups.add(psicologo_group)
#     return redirect('nuevo_psicologo') 

# @login_required
# def usuario_registrado(request):
#     if not request.user.groups.filter(name='Usuario-Registrado').exists():
#         usuario_registrado_group = Group.objects.get(name='Usuario-Registrado')
#         request.user.groups.add(usuario_registrado_group)
#     return redirect('home') 

class NuevoPsicologo(View):
    def get(self, request):
        form = FormPsicologo(initial={'user': self.request.user})
        print(form)
        return render(request, 'psicologo/psicologo_form.html', {'form': form})
    def post(self, request):
        form = FormPsicologo(request.POST)
        print(request.POST)
        print(self.request.user)

        if form.is_valid():
            nuevo_grupo, creado = Group.objects.get_or_create(name='Psicologos')
            # if creado:
            #     permiso = Permission.objects.get(codename='change_blogpost')  
            #     nuevo_grupo.permissions.add(permiso)        
            usuario = User.objects.get(username=self.request.user)
            usuario.groups.add(nuevo_grupo)    
            form.save()
            return redirect('home')
        else:
            # No necesitas iterar sobre form.error_messages
            for field, errors in form.errors.items():
                message = f"{field.capitalize()}: {errors[0]}"  # Obtén el primer error
                messages.error(request, message)
                print(message)
            return render(request, 'psicologo/psicologo_form.html', {'form': form})
    
class NuevoPaciente(CreateView):
    def get(self, request):
        form = FormPaciente(initial={'user': self.request.user})
        print(form)
        return render(request, 'paciente/paciente_form.html', {'form': form})
    def post(self, request):
        form = FormPaciente(request.POST)
        print(request.POST)
        print(self.request.user)

        if form.is_valid():
            nuevo_grupo, creado = Group.objects.get_or_create(name='Pacientes')
            # if creado:
            #     permiso = Permission.objects.get(codename='change_blogpost')  
            #     nuevo_grupo.permissions.add(permiso)        
            usuario = User.objects.get(username=self.request.user)
            usuario.groups.add(nuevo_grupo)    
            form.save()
            return redirect('home')
        else:
            # No necesitas iterar sobre form.error_messages
            for field, errors in form.errors.items():
                message = f"{field.capitalize()}: {errors[0]}"  # Obtén el primer error
                messages.error(request, message)
                print(message)
            return render(request, 'paciente/paciente_form.html', {'form': form})


class VRegistro(View):
    def get(self, request):
        form = RegistroForm()
        form.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        form.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        form.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        form.fields['first_name'].widget.attrs['placeholder'] = 'Nombre(s)'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Apellido(s)'
        form.fields['email'].widget.attrs['placeholder'] = 'Correo Electrónico'

        form.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        form.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
        form.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'
        form.fields['first_name'].widget.attrs['class'] = 'form-control form-control-user'
        form.fields['last_name'].widget.attrs['class'] = 'form-control form-control-user'
        form.fields['email'].widget.attrs['class'] = 'form-control form-control-user'
        return render(request, "registro/registro.html",{'form':form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('registro-usuario')
        else:
            # No necesitas iterar sobre form.error_messages
            for field, errors in form.errors.items():
                message = f"{field.capitalize()}: {errors[0]}"  # Obtén el primer error
                messages.error(request, message)
            return render(request, "registro/registro.html", {'form': form})
        

class RegistroUsuarioView(TemplateView):
    template_name = 'registro/registroUsuario.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Usuario-Registrado').exists():
            return redirect('home')  # Ajusta 'home' a la URL correcta
        else:
            return super().dispatch(request, *args, **kwargs)
    


 
def loguear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido.", extra_tags='error')  # Agrega este mensaje de error con etiqueta 'error'
        else:
            messages.error(request, "Información incorrecta.", extra_tags='error')  # Agrega este mensaje de error con etiqueta 'error'
    else:
        form = AuthenticationForm()
        form.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        form.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        form.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        form.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
    return render(request, "login/login.html", {'form': form})
        
def cerrarSesion(request):
    logout(request)
    return redirect('home')
    
def reestablecer_contraseña(request):
    if request.method=="POST":
            form = ReestablecerContraseñaForm(request.POST)
            if form.is_valid():
                correo = form.cleaned_data.get("email")
                usuario = authenticate(email=correo)
                if usuario is not None:
                    nuevaContraseña = form.cleaned_data.get("password1")
                    usuario.set_password(nuevaContraseña)
                    usuario.save()                                        #No reestablece la contraseña
                    return redirect('iniciar_sesion')
                else:
                    return redirect('iniciar_sesion')
                    #messages.error(request, "Correo no existente")
    else:  
            form = ReestablecerContraseñaForm()
    return render(request, "registro/reestablecer.html",{'form':form})


    
    
    
    
