Proyecto Final - Equipo 3

      Integrantes:
Lider: Jostin Ernesto Gutierrez Magaña
Carrasco Perez Sofia Elena
Jimenez Ramirez Axel Isaac
Contreras Mendiola Christian Hersaith
Serafin Lopez Alexis

Profe: JOSE CHRISTIAN ROMERO HERNANDEZ
Grupo: 4BV-PG
Fecha: 29/05/2026


# Introduccion 

En esta documentación se enfoca en nuestro proyecto final, nuestra tienda de perfumes. En el proyecto nos guiamos con actividad/proyecto individual que nos dejó nuestro profesor.
Cada parte del documento se estará hablando sobre los pasos de la creación, las modificaciones y las agregaciones que se ponen en los códigos o en la página.

Este documento tendrá la información como la información que contiene nuestro repositorio de equipo. Todo este proyecto se realizó con casi todo el equipo, cada sprint lo documentó un integrante.  

En este proyecto de venta de perfumes, todo resultó casi en su totalidad fácil, se muestra cada parte del código del programa, esto fue guiado por el sprint que el profesor ponía en su repositorio de marketplace, también algunos arreglos fueron sacados del proyecto guiado personal.


# SPRINT 1:
Aquí es donde empieza nuestro proyecto dentro del VS CODE, donde en el archivo "settings.py" declaramos  la app dentro del proyecto:


![EVIDENCIA](https://github.com/Gutierrez-Jostin/Project_perfum/blob/d0ea7d6bf60a004ec4e72a7fbc9a8b534fe5890b/Captura%20de%20pantalla%202026-05-21%20180106.png)


Como inicios de nuestro proyecto, en el archivo "models.py" donde ponemos todos los modelos de la app que tenemos hasta el momento:


![EVIDENCI2](https://github.com/Gutierrez-Jostin/Project_perfum/blob/d0ea7d6bf60a004ec4e72a7fbc9a8b534fe5890b/Captura%20de%20pantalla%202026-05-21%20183031.png)


Aquí pusimos todo lo que va dentro del admin, donde podemos controlar todo, las categorias del negocio, los productos, lo que tengas en tu carrito, etc:


![EVIDENCI3](https://github.com/Gutierrez-Jostin/Project_perfum/blob/d0ea7d6bf60a004ec4e72a7fbc9a8b534fe5890b/Captura%20de%20pantalla%202026-05-21%20183042.png)

Justo después de hacer migraciones y crear el superuser, ya podemos ingresar al admin donde podemos ver lo que guardamos en el paso anterior:


![EVIDENCI4](https://github.com/Gutierrez-Jostin/Project_perfum/blob/d0ea7d6bf60a004ec4e72a7fbc9a8b534fe5890b/Captura%20de%20pantalla%202026-05-21%20183053.png)

## Todo esto fue realizado por Sofia Carrazco, comenzando al proyecto y al administrados de este proyecto de ventas de perfumes.


# SPRINT 2

Aquí en el archivo “urls.py” del proyecto ponemos lo siguiente donde conectamos este urls con el urls de la app:


![EVIDENCI4](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/image.png)

Luego en la app creamos un archivo con el mismo nombre “urls.py” y ponemos lo siguiente donde ya tenemos conectado este urls al urls del proyecto y importamos desde views igual:

![EVIDENCIA](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20184051.png)


Ahora creamos otro archivo pero ahora llamado “forms.py” y pegamos lo siguiente que son los datos que nos pedirá a la hora de crear un user para ver si seremos clientes o vendedores:


![EVIDENCIA](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190332.png)


Aqui creamos el archivo “views.py” que es de como se vera nuestro lugar de ventas:


![EVIDENCIA](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190411.png)


Ahora después del views, creamos los templates, por el momento son los 4 básicos, ”base.html”,  “home.html”,  “login.html” y “register.html”

![EVIDENCIA](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190420.png)


Aquí ponemos cada parte de los templates que es donde va para la crear la base de los mismos 

# base.html


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190428.png)

# home.html


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190437.png)

# login.html


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190445.png)

# register.html


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190453.png)

# Esto fue hecho por Alexis Lopez, integrando los templates, el views y los urls del proyecto para que ya se pueda ingresar a la base de datos normal donde se vera la interfaz de nuestro proyecto

# SPRINT 3

Aqui hacemos una modificación en el ursl de la app agregando mas cosas sobre los productos y vendedores:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190727.png)


Aqui modificamos el archivo forms para agregarle lo de los productos


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190734.png)


Aqui es donde creamos la lógica de negocios en views, donde el user vendedor podra crear productos, editarlos y eliminarlos


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190743.png)


Despues creamos un templates llamado “deshboard.html” donde aremos un tipo amazon simple


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190752.png)


Aqui crearemos un archivo llamado “product_form.html” dentro de los templates que es oara guardar un producto


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190800.png)


Y este es para eliminar el producto, lo contrario al anterior templates, que ahora se llamara product_confirm_delete.html”


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190808.png)


Aqui agregamos esto en navbar para autenticar que si sea vendedor el user


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190815.png)


Esto fue hecho por Contreras Mendiola, mejorando la vista y la función de proyecto


# SPRINT 4:

Aqui hacemos una actualizacion al archivo “models.py” en cartItem


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20191909.png)


Aqui actualizamos en el mismo archivo en diferente parte del codigo, en cart


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20191914.png)


Ahora en el archivo “urls.py” agregamos esto que es para el carrito

![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20191957.png)


Ahora en “views.py” agregamos esto para la funcionalidad del carrito, como ver tus productos guardados, agregar nuevos o eliminar


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192005.png)


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192011.png)


Ahora aqui creamos un nuevo archivo en templates llamado “cart_detail.html” y agregamos lo siguiente donde nos dice lo que tenemos que pagar etc


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192018.png)


Ahora dentro de archivo “home.html” en templates agreganos esto de cada card


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192025.png)


Aqui agregamos el carrito  navbar, dentro del archivo “base.html” dentro de los templates


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192030.png)


# SPRINT 5


Aqui agregamos una modificacion a views.py que es para poder buscar productos en específico y ir entre paginas para ver mas productos del catálogo


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192729.png)


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192736.png)


Aqui hacemos un Home.html profesional para las busquedas por categoria


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192743.png)


Aqui agregamos algo de paginacon en home.html


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20192750.png)


# MODIFICACIONES EXTRAS BASADOS EN EL REPO DEL PROFESOR


Aqui en el archivo settings.py estamos implementando cosas para poder agregar imagenes dentro de los productos, todo esto es en el proyecto


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20193013.png)


Al igual que en el archivo urls.py modificamos y conectamos en settings.py


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/c11ec2d336ffbc7db1d36c1bedb06c63445896bd/tianguis/images/Captura%20de%20pantalla%202026-05-23%20193020.png)


En el archivo dashboard.html modificamos el codigo para que salgan las imegenes


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/28a5220e7d61adfb6ae4307ece09aa24df3c394a/tianguis/images/Captura%20de%20pantalla%202026-05-23%20193029.png)


Ahora en la app dentro del archivo forms.py agregamos esto “image en ProductForm


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/28a5220e7d61adfb6ae4307ece09aa24df3c394a/tianguis/images/Captura%20de%20pantalla%202026-05-23%20193037.png)


Aqui dentro de models.py en producto agregamos lo de image


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/28a5220e7d61adfb6ae4307ece09aa24df3c394a/tianguis/images/Captura%20de%20pantalla%202026-05-23%20193118.png)