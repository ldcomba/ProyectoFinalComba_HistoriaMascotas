# ProyectoFinalComba_HistoriaMascotas

#### orden de prueba
- [home](http://127.0.0.1:8000/home/)
	
 - [Historia de Mascotas](http://127.0.0.1:8000/AppPages/routePages/)  #En esta sección se pueden ver las distintas historias que están cargadas en la base de datos
   en el caso de estar logueado y si el usuario logueado tiene historias creadas, el mismo puede proceder a editar o eliminar la historia.
   Para ver las historias no hace falta estar logueado.
	
- [Crear Historias](http://127.0.0.1:8000/AppAccounts/login/?next=/AppPages/crearHistoria/) #En esta sección, si el usuario no está logueado, se pide que se loguee,
  una vez logueado, aparece el formulario para crear la histora.
  los usuarios no pueden cargar la imagen de la historia

- [Acerca de Mi](http://127.0.0.1:8000/AppPages/aboutMe/) #En esta sección hablo un poco de mi.

- [Loguearse](http://127.0.0.1:8000/AppAccounts/login/) #Esta es la url para loguearse

- [Registrarse](http://127.0.0.1:8000/AppAccounts/register/) #Esta es la url para registrarse

  ## una vez logueado aparencen los siguientes botones:
  - [Desloguearse]() #Con este botón los usuarios se desloguean y vuelven al home

  - [Editar perfil](http://127.0.0.1:8000/AppAccounts/editarPerfil/) #En esta sección, los usuarios pueden hacer cambiar su perfil, como descripción, avatar y demás,
    para validar los cambio se pide la contraseña actual.
    
  - [Cambiar Contraseña](http://127.0.0.1:8000/AppAccounts/cambiarPass/) #En esta sección, los usuario pueden cambiar la contraseña, poniendo la actual, y dos véces la nueva.
 
  - [Sala de Chat](http://127.0.0.1:8000/AppAccounts/chatRoom/) #A esta sección se accede haciendo click en el icono de chat, en la lista desplegable se puede elegir con que usuario chatear.
      en el desplegable están todos los usuarios menos el que está logueado. "admin-Eliana" hay conversación. Al igual que la apps de mensajería, un tilde es no leido y dos tildes es leido.
    para probar esto lo mejor es tener abierto el chat en dos navegadores distintos.

							
