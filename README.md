# Entrega final proyecto Python comisión 57810 - Alexis Marcos Ferretto

## Idea/Objetivo detras del sitio/app web
La idea detras de la app Contame es poder tener una herramienta en la cual poder cargar los gastos e ingresos personales.
Ya que no encontre actualmente ninguna app gratuita que se adapte a lo que necesito y creo que es un proyecto interesante y con mucho potencial para agregar montones de funcionalidades.
Con esto se busca poder llevar un control de los gastos por categorias (Supermercado, Servicios, Impuestos, Deporte, etc)
Tambien se busca poder tener el estado de las cuentas, como el efectivo, dineros en cuantas bancarias, fondos de inversion, etc.

Se busca una vez que se entra a la app, en el dashboard principal tener a simple vista los gastos del mes.
Mas adelante se puede poner un modelo para cargar presupuestos mensuales y tener en el dashboard el % del presupusto al día actual, para ver como se viene cumpliendo el presupuest y estar atento de no excederse.

Tambien la idea es poder tener una comparacion con meses anteriores por categoria y ver cual categoria se incremento por sobre el resto.
#

## Consignas del Proyecto Final
- Link a GitHub (https://github.com/EcoDendei/Ferretto-Alexis-57810/tree/master)
  
- Readme (Este documento)
  
- Proyecto Django
  1- Diseño no usado en clase, menu con 4 links (El diseño utilizado es una mezcla de https://startbootstrap.com/template/sb-admin y https://startbootstrap.com/theme/sb-admin-2). Los 4 links son, "Monedas", "Cuentas", "Subcuentas", "Asientos", ademas de "Dashboard" que hace a la vez de Home.
  2- Login / Logout / Registro / Modificación de Usuarios, incluyendo Avatar). Se tiene una página de login y de registro de usuario. Tambien una vez logueado y haciendo clic en el avatar, aparecen los link para ver/editar perfil, link para cambiar avatar y link para el logout.
  3- CRUD de modelos solo para usuario logueados, para los modelos de "Monedas", "Cuentas" y "Subcuentas" ademas de estar logueado se debe poder ser Staff para poder acceder a los formularios de CRUD.
  4- Link a Acerca de mi, en el footer de cada pagina se tiene un link a la página "Acerca".
  5- Formulario search, en el modelo de Cuentas se tiene una form para "Buscar Cuentas". Para el resto se utilizo la funcionalidad de buscar de las DataTables (https://datatables.net/), que es mas dinamico y preciso.

- Video, no se alcanzo a realizar Vidio explicativo.

- Excel de nombre Casos de Test.xls, el mismo se encuentra dentro del directorio principal del proyecto.

- Calidad y Legibilidad del código.
#

## Modelos
  Asiento (Algo similar a un asiento contable, se crea cuando hay algun evento que genere movimiento en las cuentas)
  Movimiento (Los movimientos de cuenta, cuando se genera un asiento la idea es generar 2 movimientos, de una cuanta se saca dinero y en otra segunda cuanta se ingresa dinero)
  Cuenta (Una categoria principal, como Salud, Deporte, Clientes, etc.)
  Subcuenta (Una subcategoria, de una categoria principal (Cuenta) como por ej. Dentista, Oculista, Padel, Futbol, etc.)
  Moneda (Ya que podemos tener movimientos es diferentes monedas)
#

## Formulario para busqueda
- cuentas/buscar-cuentas/
#

## Listado completo de funciones
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
#

## Comentarios
El modelo de "Movimiento" no tiene formularios de CRUD, estas operaciones se realizan desde el CRUD de "Asientos", por lo que cuando por ejemplo creamos un nuevo Asiento, ademas del Asiento tambien creamos 2 Movimientos.

## Orden de prueba
1 - Crear Monedas
2 - Crear Cuentas
3 - Crear Subcuentas
4 - Crear Asientos
5 - Crear Movientos

Se debe hacer en este orden ya que por ejemplo Movimiento tiene que estar vinculado a un asiento y a una cuenta que ya deben existir previamente.

## Usuarios de prueba
(Staff y Superuser) dendei - ContameApp!
(Usuario regular) User1 - TestPassOne!
