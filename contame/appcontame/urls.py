from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),
    
    
    #____ Movimientos

    
    #____ Monedas
    path('monedas/', ListaMonedas.as_view(), name="monedas"),
    path('monedas/moneda/<int:pk>', DetalleMoneda.as_view(), name="moneda"),
    path('monedas/crear-moneda/', CrearMoneda.as_view(), name="crear-moneda"),
    path('monedas/editar-moneda/<int:pk>', EditarMoneda.as_view(), name="editar-moneda"),
    path('monedas/eliminar-moneda/<int:pk>', EliminarMoneda.as_view(), name="eliminar-moneda"),
    
    #____ Subcuentas
    path('subcuentas/', ListaSubcuentas.as_view(), name="subcuentas"),
    path('subcuentas/subcuenta/<int:pk>', DetalleSubcuenta.as_view(), name="subcuenta"),
    path('subcuentas/crear-subcuenta/', CrearSubcuenta.as_view(), name="crear-subcuenta"),
    path('subcuentas/editar-subcuenta/<int:pk>', EditarSubcuenta.as_view(), name="editar-subcuenta"),
    path('subcuentas/eliminar-subcuenta/<int:pk>', EliminarSubcuenta.as_view(), name="eliminar-subcuenta"),
    
    #____ Asientos
    path('asientos/', asiento_list, name="asientos"),
    path('asientos/crear-asiento/', asientoForm, name="crear-asiento"),
    path('asientos/eliminar-asiento/<int:pk>', EliminarAsiento.as_view(), name="eliminar-asiento"),
    path('asientos/editar-asiento/<int:pk>', asientoUpdate, name="editar-asiento"),
    
    #____ Cuentas
    path('cuentas/', ListaCuentas.as_view(), name="cuentas"),
    path('cuentas/cuenta/<int:pk>', DetalleCuenta.as_view(), name="cuenta"),
    path('cuentas/crear-cuenta/', CrearCuenta.as_view(), name="crear-cuenta"),
    path('cuentas/editar-cuenta/<int:pk>', EditarCuenta.as_view(), name="editar-cuenta"),
    path('cuentas/eliminar-cuenta/<int:pk>', EliminarCuenta.as_view(), name="eliminar-cuenta"),
    path('cuentas/buscar-cuentas/', buscarCuentas, name="buscar-cuentas"),
    path('cuentas/encontrar-cuentas/', encontrarCuentas, name="encontrar-cuentas"),
    
    #____ Usuarios
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', registerRequest, name="register"),
    path('perfil/', edit_profile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar-clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar-avatar"),
]