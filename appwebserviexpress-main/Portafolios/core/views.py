from django.db.backends.utils import CursorDebugWrapper
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservadeHoraForm, BoletaForm
from django.db import connection
from .models import Reservadehora, Boleta
from usuarios.models import UsuarioWeb
from usuarios.forms import RegistrationForm

def index(request):

    return render(request,'core/index.html',{})

@login_required(login_url='/usuarios/login/')
def reserva_de_hora(request):

    form_reserva = ReservadeHoraForm()

    if request.method == 'POST':
        
        form_reserva = ReservadeHoraForm(data=request.POST)

        if form_reserva.is_valid():

            fecha_solicitud = form_reserva.data['fecha_solicitud']
            hora = form_reserva.data['hora']
            asunto = form_reserva.data['asunto']
            tiposervicio = form_reserva.data['tiposervicio']
            usuarioescritorio = form_reserva.data['usuarioescritorio']
            usuarioweb = request.user.id
            print(request.user.id)
            print(fecha_solicitud)
            print(hora)
            fecha = fecha_solicitud + ' ' + hora
            print(fecha)


            with connection.cursor() as cursor:
                cursor.callproc('PKG_RESERVADEHORA.PR_AGREGAR_RESERVADEHORA',[fecha,asunto,tiposervicio,usuarioescritorio,usuarioweb])
            
            return redirect('core:mensaje_reserva')


    return render(request,'core/reserva_de_hora.html',{'form':form_reserva})

@login_required(login_url='/usuarios/login/')
def perfil(request, id=None):
    current_user = request.user

    if id and id != current_user.id:
        user = UsuarioWeb.objects.get(id=id)
        
    else:
        
        user = current_user

    return render(request,'core/perfil.html',{'user':user})

def lista_perfil():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc()


@login_required(login_url='/usuarios/login/')
def listar_reserva_hora(request, id=None):   
    current_user = request.user

    if id and id != current_user.id:
        user = UsuarioWeb.objects.get(id=id)
        reserva = user.reserva.get(id=id)
    else:
        reserva = current_user.reserva.all()
        user = current_user

    data = {
        'reservadehora': listar_reserva()
    }

    return render(request,'core/listar_reservar_hora.html', {'data':data,'user':user, 'reserva':reserva})

def listar_reserva():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_RESERVADEHORA.PR_LISTAR_RESERVADEHORA", [out_cur])

    
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def modificar_reserva(request, id=None):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    
    reserva = Reservadehora.objects.get(id=id)

    
    formulario = ReservadeHoraForm(instance=reserva)
    
    
    if request.method == 'POST':
        formulario = ReservadeHoraForm(data=request.POST, instance=reserva)
        
        if formulario.is_valid():

            reservahora_id = reserva.id
            fecha = formulario.data['fecha_solicitud']
            asunto = formulario.data['asunto']
            tiposervicio = formulario.data['tiposervicio']
            usuarioescritorio = formulario.data['usuarioescritorio']
            usuarioweb = request.user.id

            formulario.save()
            
            return redirect('core:mensaje_modificar_reserva')
        
        
            
    return render(request,'core/modificar_reserva.html', {'formulario':formulario})



def modificar(reservahora_id,fecha,asunto,tiposervicio,usuarioescritorio,usuarioweb):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cursor.callproc('PKG_RESERVADEHORA.PR_ACTUALIZAR_RESERVADEHORA',[reservahora_id,fecha,asunto,tiposervicio,usuarioescritorio,usuarioweb])

    return cursor



def eliminar_reserva(request, id):  

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    reserva = get_object_or_404(Reservadehora, id=id)
    
    cursor.callproc('PKG_RESERVADEHORA.PR_BORRAR_RESERVADEHORA', [id])
    return redirect('core:listar_reserva')
    

def nuestros_servicios(request):


    return render(request, 'core/nuestros_servicios.html', {})


def afinacion(request):

    return render(request, 'core/afinacion.html', {})

def aire_acondicionado(request):

    return render(request, 'core/aire_acondicionado.html', {})

def alineacion(request):

    return render(request, 'core/alineacion.html', {})

def banda_de_distribucion(request):

    return render(request, 'core/banda_de_distribucion.html', {})

def bateria(request):

    return render(request, 'core/bateria.html', {})

def bomba_agua(request):

    return render(request, 'core/bomba_agua.html', {})

def caja_transferencia(request):

    return render(request, 'core/caja_transferencia.html', {})

def cambio_aceite(request):

    return render(request, 'core/cambio_aceite.html', {})

def cambio_llantas(request):

    return render(request, 'core/cambio_llantas.html', {})

def frenos(request):

    return render(request, 'core/frenos.html', {})

def direccion_hidraulica(request):

    return render(request, 'core/direccion_hidraulica.html', {})

def luces(request):

    return render(request, 'core/luces.html', {})

def boleta(request, id):
    

    boleta = Boleta.objects.get(id_user=id)    


    return render(request, 'core/boleta.html', {'boleta':boleta})

def mensaje_reserva(request):

    return render(request, 'core/mensaje_reserva.html', {})


def mensaje_modificar_reserva(request):

    return render(request, 'core/mensaje_modificar_reserva.html', {})
