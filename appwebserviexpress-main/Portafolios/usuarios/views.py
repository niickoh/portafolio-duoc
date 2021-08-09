from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login as log_in, logout as log_out
from .auth import AuthenticationEmailBackend
from django.contrib.auth import authenticate
from usuarios.models import UsuarioWeb

def register(request):

    registration_form = RegistrationForm()

    if request.method == "POST":

        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():

            user = registration_form.save()

            return redirect('usuarios:mensaje_registro')

            #username = registration_form.cleaned_data['username']
            #password = registration_form.cleaned_data['password1']

            #user = authenticate(username=username,password=password)

            #if user is not None:

                #log_in(request, user)

                #return redirect('core:index')


    return render(request, "usuarios/register.html", {'registration_form': registration_form})

def modificar_perfil(request, id):    

    perfil = UsuarioWeb.objects.get(id=id)

    formulario = RegistrationForm(instance=perfil)

    if request.method == 'POST':
        formulario = RegistrationForm(data=request.POST, instance=perfil)

        if formulario.is_valid():            

            formulario.save()           

            return redirect('core:perfil')



    return render(request, 'usuarios/modificar_perfil.html', {'form':formulario})


def mensaje_registro(request):

    return render(request,'usuarios/mensaje_registro.html',{})


def login(request):

    login_form = LoginForm()

    if request.method == "POST":
        print('pasa')
        login_form = LoginForm(data=request.POST)

        print(login_form.is_valid())
        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:

                log_in(request, user)

                return redirect('core:index')

            user = AuthenticationEmailBackend(username=username, password=password)

            if user is not None:

                log_in(request, user)

                return redirect('core:index')

    return render(request, 'usuarios/login.html',{'login_form':login_form})

def logout(request):

    log_out(request)

    return redirect('usuarios:inicio_sesion')
