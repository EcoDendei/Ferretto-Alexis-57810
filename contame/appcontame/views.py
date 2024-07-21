from django.core.exceptions import ObjectDoesNotExist
#from django.utils.timezone import *
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #Trabajan sobre las clases
from django.contrib.auth.decorators import login_required #Trabajan sobre las funciones
from django.contrib.admin.views.decorators import staff_member_required

from .models import *
from .forms import *

# Funciones para validar que puede ver el usuario dependiendo si es Staff


# Vistas CRUD de Cuentas
class ListaCuentas(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Cuenta
    context_object_name = 'cuentas'
    
    def test_func(self):
        return self.request.user.is_staff

class DetalleCuenta(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Cuenta
    context_object_name = 'cuenta'

    def test_func(self):
        return self.request.user.is_staff
    

class CrearCuenta(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Cuenta
    fields = '__all__'
    success_url = reverse_lazy('cuentas')
    
    def get_success_url(self):
        if "crear-uno-mas" in self.request.POST:
            return reverse_lazy('crear-cuenta')
        return super().get_success_url()
    
    def test_func(self):
        return self.request.user.is_staff
    
    
class EditarCuenta(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cuenta
    fields = '__all__'
    success_url = reverse_lazy('cuentas')

    def test_func(self):
        return self.request.user.is_staff
    

class EliminarCuenta(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cuenta
    context_object_name = 'cuenta'
    success_url = reverse_lazy('cuentas')

    def test_func(self):
        return self.request.user.is_staff
    

# Vistas CRUD de Monedas
class ListaMonedas(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Moneda
    context_object_name = 'monedas'

    def test_func(self):
        return self.request.user.is_staff


class DetalleMoneda(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Moneda
    context_object_name = 'moneda'
    
    def test_func(self):
        return self.request.user.is_staff
    

class CrearMoneda(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Moneda
    fields = '__all__'
    success_url = reverse_lazy('monedas')
    
    def test_func(self):
        return self.request.user.is_staff
    
    
class EditarMoneda(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Moneda
    fields = '__all__'
    success_url = reverse_lazy('monedas')
    def test_func(self):
        
        return self.request.user.is_staff


class EliminarMoneda(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Moneda
    context_object_name = 'moneda'
    success_url = reverse_lazy('monedas')
    
    def test_func(self):
        return self.request.user.is_staff


# Vistas CRUD de Subcuenta #
class ListaSubcuentas(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Subcuenta
    context_object_name = 'subcuentas'
    
    def test_func(self):
        return self.request.user.is_staff


class DetalleSubcuenta(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Subcuenta
    context_object_name = 'subcuenta'
    
    def test_func(self):
        return self.request.user.is_staff


class CrearSubcuenta(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Subcuenta
    fields = '__all__'
    success_url = reverse_lazy('subcuentas')

    def test_func(self):
        return self.request.user.is_staff
    
    
class EditarSubcuenta(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subcuenta
    fields = '__all__'
    success_url = reverse_lazy('subcuentas')
    
    def test_func(self):
        return self.request.user.is_staff


class EliminarSubcuenta(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subcuenta
    context_object_name = 'subcuenta'
    success_url = reverse_lazy('subcuentas')
    
    def test_func(self):
        return self.request.user.is_staff


# Vistas CRUD de Asientos #
class EliminarAsiento(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Asiento
    context_object_name = 'asiento'
    success_url = reverse_lazy('asientos')
    
    def test_func(self):
        staff = self.request.user.is_staff
        asiento = self.get_object()
        owner = True if asiento.usuario_id == self.request.user.id else False
        return staff or owner


@login_required
def asiento_list(request):
    contexto = {"asientos": Asiento.objects.select_related().all()}
    
    return render(request, "appcontame/asiento_list.html", contexto)

@login_required
def asientoForm(request):
    if request.method == 'POST':
        mi_form = AsientoForm(request.POST)
        if mi_form.is_valid():
            asiento_fecha = mi_form.cleaned_data.get("fecha")
            asiento_desc = mi_form.cleaned_data.get("desc")
            asiento_activo = mi_form.cleaned_data.get("activo")
            asiento_cuenta_origen = mi_form.cleaned_data.get("cuenta_origen")
            asiento_monto_origen = mi_form.cleaned_data.get("monto_origen")
            asiento_cuenta_destino = mi_form.cleaned_data.get("cuenta_destino")
            asiento_monto_destino = mi_form.cleaned_data.get("monto_destino")
            asiento_usuario = request.user.id
                    
            asiento = Asiento(fecha=asiento_fecha, desc=asiento_desc, activo=asiento_activo, usuario_id = asiento_usuario)
            asiento.save()
            
            movimiento_origen = Movimiento(asiento=asiento, monto=asiento_monto_origen*-1, cuenta=asiento_cuenta_origen)
            movimiento_origen.save()
            
            movimiento_destino = Movimiento(asiento=asiento, monto=asiento_monto_destino, cuenta=asiento_cuenta_destino)
            movimiento_destino.save()
            
            contexto = {"asientos": Asiento.objects.all()}
            return redirect(reverse_lazy('asientos'))
    else:
        mi_asiento_form = AsientoForm()
        
    return render(request, "appcontame/asiento_form.html", {"form": mi_asiento_form})


@login_required
def asientoUpdate(request, pk):
    asiento = Asiento.objects.get(id=pk)
    
    if asiento.usuario_id != request.user.id and not request.user.is_staff:
        return redirect(reverse_lazy('asientos'))
    
    movimiento_origen = Movimiento.objects.filter(asiento_id=pk).first()
    movimiento_destino = Movimiento.objects.filter(asiento_id=pk).last()
    
    if request.method == 'POST':
        mi_form = AsientoForm(request.POST)
        if mi_form.is_valid():
            
            asiento.fecha = mi_form.cleaned_data.get("fecha")
            asiento.desc = mi_form.cleaned_data.get("desc")
            asiento.activo = mi_form.cleaned_data.get("activo")
            movimiento_origen.cuenta = mi_form.cleaned_data.get("cuenta_origen")
            movimiento_origen.monto = mi_form.cleaned_data.get("monto_origen") * -1
            movimiento_destino.cuenta = mi_form.cleaned_data.get("cuenta_destino")
            movimiento_destino.monto = mi_form.cleaned_data.get("monto_destino")

            asiento.save()
            movimiento_origen.save()
            movimiento_destino.save()
            
            return redirect(reverse_lazy('asientos'))
    else:
        mi_asiento_form = AsientoForm(initial={"fecha":asiento.fecha, "desc":asiento.desc, "cuenta_origen":movimiento_origen.cuenta, "monto_origen":movimiento_origen.monto*-1, "cuenta_destino":movimiento_destino.cuenta, "monto_destino":movimiento_destino.monto, "activo":asiento.activo})
        
    return render(request, "appcontame/asiento_form.html", {"form": mi_asiento_form})


def ingreso_mes_actual():
    
    mes_actual = datetime.datetime.now().month
    ingreso_mes = Movimiento.objects.select_related().filter(asiento__fecha__month=mes_actual, cuenta__tipo="INGRESO").aggregate(Sum("monto"))
    
    return ingreso_mes["monto__sum"]*-1


def ingreso_anio_actual():
    
    anio_actual = datetime.datetime.now().year
    ingreso_anio = Movimiento.objects.select_related().filter(asiento__fecha__year=anio_actual, cuenta__tipo="INGRESO").aggregate(Sum("monto"))
    
    return ingreso_anio["monto__sum"]*-1


def egreso_mes_actual():
    
    mes_actual = datetime.datetime.now().month
    egreso_mes = Movimiento.objects.select_related().filter(asiento__fecha__month=mes_actual, cuenta__tipo="EGRESO").aggregate(Sum("monto"))
    
    return egreso_mes["monto__sum"]


def egreso_anio_actual():
    
    anio_actual = datetime.datetime.now().year
    egreso_anio = Movimiento.objects.select_related().filter(asiento__fecha__year=anio_actual, cuenta__tipo="EGRESO").aggregate(Sum("monto"))
    
    return egreso_anio["monto__sum"]


def ganancia_mes_actual():
    
    ganancia_mes = ingreso_mes_actual() - egreso_mes_actual()
    
    return ganancia_mes


def ganancia_anio_actual():
    
    ganancia_anio = ingreso_anio_actual() - egreso_anio_actual()
    
    return ganancia_anio


# Pagina principal view
def home(request):
    
    #Traer ingresos del mes
    ingreso_mensual = ingreso_mes_actual()
    #Traer ingresos del año
    ingreso_anual = ingreso_anio_actual()
    
    #Traer egresos del mes
    egreso_mensual = egreso_mes_actual()
    #Traer egresos del año
    egreso_anual = egreso_anio_actual()
    
    #Traer ganancias del mes
    ganancia_mensual = ganancia_mes_actual()
    #Traer ganancias del año
    ganancia_anual = ganancia_anio_actual()
    
    return render(request, "appcontame/index.html", {"ingreso_mensual": ingreso_mensual, "ingreso_anual": ingreso_anual, "egreso_mensual": egreso_mensual, "egreso_anual": egreso_anual, "ganancia_mensual": ganancia_mensual, "ganancia_anual": ganancia_anual})


def acerca(request):
    return render(request, "appcontame/acerca.html")


# Seccion de busquedas
def buscarCuentas(request):
    return render(request, "appcontame/buscar.html")


def encontrarCuentas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cuentas = Cuenta.objects.filter(nombre__icontains=patron) 
    else:
        cuentas = Cuenta.objects.all()
        
    contexto = {'cuentas': cuentas}
    return render(request, "appcontame/cuenta_list.html", contexto)


# MANAJO DE USUARIO - LOGIN/LOGOUT/REGISTER #
def loginRequest(request):
    
    if request.method == "POST":
        
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            #Obtener avatar del usuario
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except ObjectDoesNotExist:
                avatar = "/media/avatares/undraw_rocket.svg"
            finally:
                request.session["avatar"] = avatar
            
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('login'))
        
    else:
        mi_form = LoginForm()
    
    return render(request, "appcontame/login.html", {"form": mi_form})


def registerRequest(request):
    
    if request.method == "POST":
        
        mi_form = RegistroForm(request.POST)
        
        if mi_form.is_valid():
            mi_form.save()
            return redirect(reverse_lazy('login'))
    else:
        mi_form = RegistroForm()
            
    return render(request, "appcontame/register.html", {"form": mi_form})


@login_required
def edit_profile(request):
    usuario = request.user
    if request.method == "POST":
        mi_form = UserEditForm(request.POST)
        if mi_form.is_valid():
            user = User.objects.get(username=usuario)
            user.email = mi_form.cleaned_data.get("email")
            user.first_name = mi_form.cleaned_data.get("first_name")
            user.last_name = mi_form.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        mi_form = UserEditForm(instance=usuario)
    return render(request, "appcontame/editar_perfil.html", {"form": mi_form})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "appcontame/cambiar_clave.html"
    success_url = reverse_lazy("home")
    

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
        mi_form = AvatarForm(request.POST, request.FILES)
        if mi_form.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = mi_form.cleaned_data["imagen"]
            
            #Borrar avatares viejos
            avatar_viejo = Avatar.objects.filter(user=usuario)
            
            if len(avatar_viejo) > 0:
                for i in range(len(avatar_viejo)):
                    avatar_viejo[i].delete()
            
            #Guardar avatar nuevo
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            #Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        mi_form = AvatarForm()
    return render(request, "appcontame/avatar_perfil.html", {"form": mi_form})