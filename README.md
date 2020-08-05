# refugio-mascotas
Web App de administración centro de adopción de mascotas

### Descripción y contexto
---
Web App que permite el gestionamiento para adopciones de mascotas mediante solicitudes Padrino (para dar en adopción) ó Adoptante (solicitar adopción), implementando un panel de control y registro de las solicitudes, personas, mascotas, noticias, entre otras mediante usuarios que requieren autenticación.

Contiene una sección de posts principalmente para noticias tipo Blog, apartado de Contacto (a configurar), entre otros.

### Guía de usuario
---
Por default el proyecto tiene un User: "admin" y un password: "Jhonatan_09" para ingresar al panel de administración.

El resto de las funcionalidades deberá usarse intuitivamente. 
 	
### Guía de instalación
---
El proyecto raiz esta hecho principalmente en Django y Django REST Framework para el backend, el frontend está alojado por completo en la carpeta con dicho nombre el cual se trabajo con VueJS.

El proyecto está hecho para que Django tenga implementado el frontend a través de todo el compilado de Vue alojado en la carpeta frontend/dist, teniendo dentro de esta misma la carpeta /static donde se ecuentran los archivos estaticos tanto para Django como para Vue.
Por lo anterior es de suma importancia adverir que antes de volver a compilar el frontend (por modificaciones u otras razones), se debe configurar Vue para no elimine la carpeta /static ya que borraría los archivos correspondientes a Django.

luego de instalar el repositorio, verificar las dependencias para actualizar y/o instalar las mencionadas necesarias en el apartado #Dependencias.
Posteriormente ejecutar el servidor para dajngo mediante el siguiente comando Python desde el directorio creado:

    Python manage.py runserver.

#### Dependencias
Librerías, frameworks, acceso a bases de datos donde ha sido probada la herramienta digital. 

Entorno Backend:

    Python 3.8.2.
    Django 3.0.5

Paquetes en Django:

    rest_framework
    corsheaders
    allauth
    ckeditor
    
Entorno Frontend:

    Vue 2.6.11
    Vue-axios 2.1.5
    Vue-prism-component 1.2.0
    Vue-router 3.2.0
    Vue-sweetalert2 3.0.6
    Vuex 3.4.0
    bootstrap-vue 2.15.0
    core-js 3.6.5
    jwt-decode 2.2.0
    prismjs 1.20.0
    animate.css 4.1.0
    axios 0.19.2
    
Data Base:

    PostgresSQL

### Autor
---

JHOJANY UZCATEGUI

Correo: jhojaforce@gmail.com

Linkedin: https://www.linkedin.com/in/jhojany-jose-uzcategui-araujo-879b82130/


### Licencia 
---
[LICENCIA](https://github.com/lextomato/refugio-mascotas/blob/master/LICENSE.md)

## Limitación de responsabilidades

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.
