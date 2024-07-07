# IS2_Extra

## Grupo8_Relecloud

### Autores del proyecto:

	- Carlos García Revillas (Parte 1)

	- Carlos Peraza García (Parte 3)

	- Álvaro Salvador López (Parte 4)

	- Antonio Serra García de Eulate (Parte 2)

### Descripción del proyecto:

	Repositorio para la extensión del proyecto Django 'Relecloud' desde Azure DevOps. Este proyecto 
	fue desarrollado en equipo, con cada miembro del grupo contribuyendo a diferentes funcionalidades 
	específicas para mejorar la aplicación. Cada parte no solo añadió características útiles sino que 
	también aseguró que el proyecto pudiera escalar y ser mantenido de manera eficiente.

### Desarrollo del poryecto:

	Parte 1.- Añadir Opción de Opiniones en el Menú:

	 - Responsable: Carlos García Revillas

	 - Contribución: Implementación de una funcionalidad de opinión que permite a los usuarios compartir
	   feedback de los cruceros, mejorando la interactividad del sitio.

	 - Impacto: Aumento de la participación del usuario y mejora en la calidad del servicio basado en el 
	   feedback recibido.


	Parte 2.- Modificar para Añadir Opiniones:

     - Responsable: Antonio Serra García de Eulate

	 - Contribución: Desarrollo de la funcionalidad para que los usuarios añadan sus propias opiniones, 
	   ayudando así a tener una comunidad más activa.

	 - Impacto: Mejora directa en la funcionalidad del sitio, permitiendo una experiencia de usuario más 
	   rica y personalizada. Los usuarios pueden añadir opiniones a través del formulario y estas opiniones 
	   se guardan y muestran correctamente.


	Parte 3.- Añadir Fotografías a los Destinos:

	 - Responsable: Carlos Peraza García

	 - Descripción: Mejora de la página de destinos con imágenes, proporcionando un contexto visual que ayuda
	   a la usabilidad del servicio y el atractivo del sitio.

	 - Impacto: Aumenta el atractivo del sitio que puede traducirse en un mayor tiempo de permanencia en la 
	   página. Las imágenes de los destinos se muestran junto con la descripción y los cruceros asociados.


	Parte 4.- Envío de Notificaciones por Correo:

	 - Responsable: Álvaro Salvador López

	 - Contribución: Integración de notificaciones por correo electrónico para confirmar las solicitudes de 
	   información, mejorando la comunicación con el usuario.

     - Validación: Asegura una interacción eficaz con los usuarios, aumentando su satisfacción y confianza en 
	   el servicio.

### Uso de Azure para el despliegue

	El proyecto se despliega a través de Azure App Services, lo que permite un escalado fácil y un mantenimiento 
	eficiente. Utilizamos Azure Pipelines para un despliegue continuo desde el repositorio de Git hasta la producción.
	Esto incluye la integración de pruebas automáticas que garantizan la calidad del software antes de cada despliegue.

 	 - Base de Datos PostgreSQL Flexible:

	 	+ Configuración: Utilizamos Azure Database for PostgreSQL Flexible Server para gestionar las bases de datos del proyecto.

		+ Ventajas: Ofrece alta disponibilidad, escalabilidad sin interrupciones y configuraciones de seguridad avanzadas
		  que son esenciales para la protección de los datos de los usuarios.


### Despliegue Mediante Pipeline:

	El pipeline de CI/CD configurado en Azure DevOps compila el proyecto, ejecuta pruebas y despliega la aplicación en 
	Azure App Service automáticamente tras cada commit. Esto minimiza el tiempo de despliegue y los errores humanos asociados
	con el despliegue manual.
