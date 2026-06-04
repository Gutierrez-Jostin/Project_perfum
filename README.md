Proyecto Final - Equipo 3

Integrantes:

Lider: Jostin Ernesto Gutierrez Magaña

1-Carrazco Perez Sofia Elena

2--Jimenez Ramirez Axel Isaac

3-Contreras Mendiola Christian Hersaith

4-Serafin Lopez Alexis



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


```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
# Aqui ponemos el nombre de la app
    'tianguis'
]
# Y aquí el modelo de user en tianguis
AUTH_USER_MODEL = 'tianguis.User'

```


Como inicios de nuestro proyecto, en el archivo "models.py" donde ponemos todos los modelos de la app que tenemos hasta el momento:


```Python 
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# =========================
# 👤 Usuario
# =========================
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# =========================
# 🏷️ Categoría
# =========================
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# =========================
# 📦 Producto
# =========================
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )  # 1:N

    categories = models.ManyToManyField(
        Category,
        related_name='products'
    )  # N:M

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# 🛒 Carrito
# =========================
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts'
    )  # 1:N

    products = models.ManyToManyField(
        Product,
        through='CartItem',
        related_name='carts'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user}"
    @property
    def total(self):
        return sum(item.subtotal for item in self.cartitem_set.all())


# =========================
# 🧾 CartItem (tabla intermedia)
# =========================
class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.product} x {self.quantity}"

```


Aquí pusimos todo lo que va dentro del admin, donde podemos controlar todo, las categorias del negocio, los productos, lo que tengas en tu carrito, etc:


```Python
from django.contrib import admin
from .models import User, Category, Product, Cart, CartItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_seller')
    list_filter = ('is_seller',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'owner')
    list_filter = ('categories',)
    search_fields = ('name',)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    inlines = [CartItemInline]

```

Justo después de hacer migraciones y crear el superuser, ya podemos ingresar al admin donde podemos ver lo que guardamos en el paso anterior:


![EVIDENCI4](https://github.com/Gutierrez-Jostin/Project_perfum/blob/d0ea7d6bf60a004ec4e72a7fbc9a8b534fe5890b/Captura%20de%20pantalla%202026-05-21%20183053.png)

 Todo esto fue realizado por Sofia Carrazco, comenzando al proyecto y al administrados de este proyecto de ventas de perfumes.


# SPRINT 2

Aquí en el archivo “urls.py” del proyecto ponemos lo siguiente donde conectamos este urls con el urls de la app:


```Python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tianguis.urls')),
]

```

Luego en la app creamos un archivo con el mismo nombre “urls.py” y ponemos lo siguiente donde ya tenemos conectado este urls al urls del proyecto y importamos desde views igual:

```Python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

```


Ahora creamos otro archivo pero ahora llamado “forms.py” y pegamos lo siguiente que son los datos que nos pedirá a la hora de crear un user para ver si seremos clientes o vendedores:


```Python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_seller = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_seller', 'password1', 'password2')
```


Aqui creamos el archivo “views.py” que es de como se vera nuestro lugar de ventas:


```Python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from .models import Product


def home(request):
    products = Product.objects.select_related('owner').prefetch_related('categories').all()
    return render(request, 'tianguis/home.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'tianguis/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'tianguis/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

```


Ahora después del views, creamos los templates, por el momento son los 4 básicos, ”base.html”,  “home.html”,  “login.html” y “register.html”

![EVIDENCIA](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b432fa7dfbf96184a4a98b3dfd06182d96a20641/tianguis/images/Captura%20de%20pantalla%202026-05-23%20190420.png)


Aquí ponemos cada parte de los templates que es donde va para la crear la base de los mismos 

# base.html


```Python
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Marketplace</title>

    <!-- Bootstrap 5.3 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="/">Marketplace</a>

    <div>
      {% if user.is_authenticated %}
        <span class="text-white me-3">Hola {{ user.username }}</span>
        <a href="{% url 'logout' %}" class="btn btn-outline-light btn-sm">Logout</a>
      {% else %}
        <a href="{% url 'login' %}" class="btn btn-outline-light btn-sm me-2">Login</a>
        <a href="{% url 'register' %}" class="btn btn-primary btn-sm">Registro</a>
      {% endif %}
    </div>
  </div>
</nav>

<div class="container mt-4">
    {% block content %}{% endblock %}
</div>

</body>
</html>

```

# home.html


```Python
{% extends 'tinaguis/base.html' %}

{% block content %}

<h2 class="mb-4">Productos</h2>

<div class="row">
    {% for product in products %}
    <div class="col-md-4">
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5>{{ product.name }}</h5>
                <p>{{ product.description|truncatechars:80 }}</p>

                <p><strong>$ {{ product.price }}</strong></p>

                <small class="text-muted">
                    Vendedor: {{ product.owner.username }}
                </small>

                <div class="mt-2">
                    {% for cat in product.categories.all %}
                        <span class="badge bg-secondary">{{ cat.name }}</span>
                    {% endfor %}
                </div>

            </div>
        </div>
    </div>
    {% empty %}
        <p>No hay productos aún.</p>
    {% endfor %}
</div>

{% endblock %}

```

# login.html


```Python
{% extends 'tianguis/base.html' %}

{% block content %}

<h2>Login</h2>

<form method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Usuario" class="form-control mb-2">
    <input type="password" name="password" placeholder="Contraseña" class="form-control mb-2">

    <button class="btn btn-primary">Ingresar</button>
</form>

{% endblock %}

```

# register.html


```Python
{% extends 'tianguis/base.html' %}

{% block content %}

<h2>Registro</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}

    <button class="btn btn-success">Registrarse</button>
</form>

{% endblock %}

```

 Esto fue hecho por Alexis Lopez, integrando los templates, el views y los urls del proyecto para que ya se pueda ingresar a la base de datos normal donde se vera la interfaz de nuestro proyecto

# SPRINT 3

Aqui hacemos una modificación en el ursl de la app agregando mas cosas sobre los productos y vendedores:


```Python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Vendedores
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # La creacion, modificacion y eliminacion de productos
    # Productos CRUD
    path('products/create/', views.product_create, name='product_create'),
    path('products/<uuid:pk>/edit/', views.product_update, name='product_update'),
    path('products/<uuid:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Cart
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<uuid:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<uuid:item_id>/', views.update_cart_item, name='update_cart_item'),

]

```


Aqui modificamos el archivo forms para agregarle lo de los productos


```Python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Product

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_seller = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_seller', 'password1', 'password2')
        
# Agregamos esto        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }

```


Aqui es donde creamos la lógica de negocios en views, donde el user vendedor podra crear productos, editarlos y eliminarlos


```Python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ProductForm
from .models import Product

# =========================
# 📊 Dashboard
# =========================
@login_required
def dashboard(request):
    if not request.user.is_seller:
        return HttpResponseForbidden("No tienes permisos")

    products = Product.objects.filter(owner=request.user)

    return render(request, 'tianguis/dashboard.html', {
        'products': products
    })


# =========================
# ➕ Crear producto
# =========================
@login_required
def product_create(request):
    if not request.user.is_seller:
        return HttpResponseForbidden("Solo vendedores")

    form = ProductForm(request.POST or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user
        product.save()
        form.save_m2m()

        return redirect('dashboard')

    return render(request, 'tianguis/product_form.html', {'form': form})


# =========================
# ✏️ Editar producto
# =========================
@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.owner != request.user:
        return HttpResponseForbidden("No puedes editar este producto")

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'tianguis/product_form.html', {'form': form})


# =========================
# 🗑️ Eliminar producto
# =========================
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.owner != request.user:
        return HttpResponseForbidden("No puedes eliminar este producto")

    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')

    return render(request, 'tianguis/product_confirm_delete.html', {'product': product})

```


Despues creamos un templates llamado “deshboard.html” donde aremos un tipo amazon simple


```Python
{% extends 'tianguis/base.html' %}

{% block content %}

<div class="d-flex justify-content-between align-items-center mb-4">
    <h2>Mi Dashboard</h2>
    <a href="{% url 'product_create' %}" class="btn btn-success">+ Nuevo Producto</a>
</div>

<table class="table table-striped">
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Stock</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>

    {% for product in products %}
        <tr>
            <td>{{ product.name }}</td>
            <td>$ {{ product.price }}</td>
            <td>{{ product.stock }}</td>
            <td>
                <a href="{% url 'product_update' product.id %}" class="btn btn-warning btn-sm">Editar</a>

                <a href="{% url 'product_delete' product.id %}" class="btn btn-danger btn-sm">Eliminar</a>
            </td>
        </tr>
    {% endfor %}

    </tbody>
</table>

{% endblock %}

```


Aqui crearemos un archivo llamado “product_form.html” dentro de los templates que es oara guardar un producto


```Python
{% extends 'tianguis/base.html' %}

{% block content %}

<h2>Producto</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}

    <button class="btn btn-primary">Guardar</button>
</form>

{% endblock %}

```


Y este es para eliminar el producto, lo contrario al anterior templates, que ahora se llamara "product_confirm_delete.html”


```Python
{% extends 'tianguis/base.html' %}

{% block content %}

<h3>¿Eliminar "{{ product.name }}"?</h3>

<form method="POST">
    {% csrf_token %}
    <button class="btn btn-danger">Sí, eliminar</button>
    <a href="{% url 'dashboard' %}" class="btn btn-secondary">Cancelar</a>
</form>

{% endblock %}

```


Aqui agregamos esto en navbar para autenticar que si sea vendedor el user


```Python
{% if user.is_authenticated and user.is_seller %}
    <a href="{% url 'dashboard' %}" class="btn btn-warning btn-sm me-2">Dashboard</a>
{% endif %}

```


Esto fue hecho por Contreras Mendiola, mejorando la vista y la función de proyecto


# SPRINT 4:

Aqui hacemos una actualizacion al archivo “models.py” en cartItem


```Python
# Actualizar
    @property
        def subtotal(self):
            return self.product.price * self.quantity

        def __str__(self):
            return f"{self.product} x {self.quantity}"

```


Aqui actualizamos en el mismo archivo en diferente parte del codigo, en cart


```Python
# Actualizar    
    @property
    def total(self):
        return sum(item.subtotal for item in self.cartitem_set.all())

```


Ahora en el archivo “urls.py” agregamos esto que es para el carrito

```Python
  # Este es el carro
    # Cart
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<uuid:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<uuid:item_id>/', views.update_cart_item, name='update_cart_item'),

```


Ahora en “views.py” agregamos esto para la funcionalidad del carrito, como ver tus productos guardados, agregar nuevos o eliminar


```Python
from .models import Cart, CartItem

# =========================
# 🛒 Ver carrito
# =========================
@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    return render(request, 'tianguis/cart_detail.html', {
        'cart': cart
    })


# =========================
# ➕ Agregar producto
# =========================
@login_required
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(
            user=request.user
        )

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


# =========================
# ❌ Eliminar item
# =========================
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect('cart_detail')


# =========================
# 🔄 Actualizar cantidad
# =========================
@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()

    return redirect('cart_detail')

```


Ahora aqui creamos un nuevo archivo en templates llamado “cart_detail.html” y agregamos lo siguiente donde nos dice lo que tenemos que pagar etc


```Python
{% extends 'tianguis/base.html' %}

{% block content %}

<h2 class="mb-4">Mi Carrito</h2>

{% if cart.cartitem_set.all %}

<table class="table table-bordered align-middle">
    <thead>
        <tr>
            <th>Producto</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Subtotal</th>
            <th></th>
        </tr>
    </thead>

    <tbody>

    {% for item in cart.cartitem_set.all %}
        <tr>

            <td>{{ item.product.name }}</td>

            <td>$ {{ item.product.price }}</td>
            <td>
                <form method="POST"
                      action="{% url 'update_cart_item' item.id %}">
                    {% csrf_token %}

                    <input type="number"
                           name="quantity"
                           value="{{ item.quantity }}"
                           min="1"
                           class="form-control"
                           style="width:90px;">

                    <button class="btn btn-sm btn-primary mt-2">
                        Actualizar
                    </button>
                </form>
            </td>

            <td>
                $ {{ item.subtotal }}
            </td>

            <td>
                <a href="{% url 'remove_from_cart' item.id %}"
                   class="btn btn-danger btn-sm">
                    Eliminar
                </a>
            </td>

        </tr>
    {% endfor %}

    </tbody>
</table>

<div class="text-end">
    <h3>Total: $ {{ cart.total }}</h3>
</div>

{% else %}

<div class="alert alert-info">
    Tu carrito está vacío
</div>

{% endif %}

{% endblock %}

```


Ahora dentro de archivo “home.html” en templates agreganos esto de cada card


```Python
{% if user.is_authenticated %}
    <a href="{% url 'add_to_cart' product.id %}"
       class="btn btn-success mt-3">
       Agregar al carrito
    </a>
{% endif %}

```


Aqui agregamos el carrito  navbar, dentro del archivo “base.html” dentro de los templates


```Python
<a href="{% url 'cart_detail' %}"
   class="btn btn-outline-light btn-sm me-2">
   Carrito
</a>

```


# SPRINT 5


Aqui agregamos una modificacion a views.py que es para poder buscar productos en específico y ir entre paginas para ver mas productos del catálogo


```Python
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Category

def home(request):

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.select_related(
        'owner'
    ).prefetch_related(
        'categories'
    ).all()

    # =========================
    # 🔎 Busqueda
    # =========================
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # =========================
    # 🏷️ Filtro categoria
    # =========================
    if category_id:
        products = products.filter(
            categories__id=category_id
        )

    # =========================
    # 📄 Paginacion
    # =========================
    paginator = Paginator(products, 6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'tianguis/home.html', {
        'page_obj': page_obj,
        'categories': categories,
        
    })

```



Aqui hacemos un Home.html profesional para las busquedas por categoria


```Python
{% extends 'tianguis/base.html' %}

{% block content %}
<form method="GET" class="row mb-4">
    <div class="col-md-5">
        <input type="text"
               name="q"
               class="form-control"
               placeholder="Buscar productos..."
               value="{{ request.GET.q }}">
    </div>

    <div class="col-md-4">
        <select name="category"
                class="form-select">
            <option value="">Todas las categorías</option>
            {% for category in categories %}
                <option value="{{ category.id }}" {% if request.GET.category|add:"0" == category.id %}selected{% endif %}>
                    {{ category.name }}
                </option>
            {% endfor %}
        </select>
    </div>

    <div class="col-md-3">
        <button class="btn btn-dark w-100">
            Buscar
        </button>
    </div>
</form>

```


Aqui agregamos algo de paginacion en home.html


```Python
{% if page_obj.has_other_pages %}
    <nav aria-label="Paginación de productos" class="mt-5">
        <ul class="pagination justify-content-center"> 
            {% if page_obj.has_previous %}
                <li class="page-item">
                    <a class="page-link" 
                       href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                       &laquo; Anterior
                    </a>
                </li>
            {% else %}
                <li class="page-item disabled">
                    <span class="page-link">&laquo; Anterior</span>
                </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
                {% if page_obj.number == num %}
                    <li class="page-item active">
                        <span class="page-link">{{ num }}</span>
                    </li>
                {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                    <li class="page-item">
                        <a class="page-link" 
                           href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                           {{ num }}
                        </a>
                    </li>
                {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
                <li class="page-item">
                    <a class="page-link" 
                       href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                       Siguiente &raquo;
                    </a>
                </li>
            {% else %}
                <li class="page-item disabled">
                    <span class="page-link">Siguiente &raquo;</span>
                </li>
            {% endif %}
            
        </ul>
    </nav>
    {% endif %}

```


# MODIFICACIONES EXTRAS BASADOS EN EL REPO DEL PROFESOR


Aqui en el archivo settings.py estamos implementando cosas para poder agregar imagenes dentro de los productos, todo esto es en el proyecto


```Python
STATIC_URL = 'static/'
# Actualizar
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

```


Al igual que en el archivo urls.py modificamos y conectamos en settings.py


````Python
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tianguis.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

````


En el archivo dashboard.html modificamos el codigo para que salgan las imegenes


```Python
{% if product.image %}
                            <img src="{{ product.image.url }}" 
                                 alt="{{ product.name }}" 
                                 class="img-thumbnail" 
                                 style="width: 60px; height: 60px; object-fit: cover;">
                        {% else %}
                            <div class="bg-light d-flex align-items-center justify-content-center border rounded" 
                                 style="width: 60px; height: 60px;">
                                <small class="text-muted">N/A</small>
                            </div>
                        {% endif %}

```


Ahora en la app dentro del archivo forms.py agregamos esto “image en ProductForm


```Python
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        # Aqui agregamos el 'image'
        fields = ['name', 'description', 'price', 'stock', 'categories', 'image']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }

```


Aqui dentro de models.py en producto agregamos lo de image


```Python
# =========================
# 📦 Producto
# =========================
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    # Agregar image
    image = models.ImageField(upload_to='upload/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

```


# Admin

Aquí vemos los cuatro modelos del admin, que son los Usuarios, los productos, las categorías y el carrito


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin1.png)



Users:
Aquí estamos en usuarios, donde podemos ver si el usuario es vendedor o comprador, vendedor seria “IS SELLER”, esto es importante por que uno puede subir productos y el otro solo comprar


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin2.png)



Productos:
Aqui en productos, es donde vemos cada uno de los productos que el usuario vendedor agregó para que salga en la página web


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin3.png)


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin4.png)



Categorías:
Aqui en categorías es donde ponemos la categoría en la que pertenece cada producto, en nuestro caso, la marca de nuestro producto, ya que aunque son el mismo producto, son de diferente marca y asi podremos facilitar su búsqueda


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin5.png)



Carritos:
Aquí en cart, vemos el carrito de cada user, donde podemos ver los productos que el usuario tiene en su carrito de compra


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin6.png)



Carrito sin producto:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin7.png)



Carrito con producto:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/admin8.png)




# Página web:

Esta es nuestra tienda virtual de perfumes, donde el cliente puede ver nuestros productos, buscar por marca(categoría) o por producto, y donde puede agregar al carrito etc, en este caso vemos desde la cuenta de vendedor, por eso la opción del Dashboard


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web1.png)



Búsquedas: 
Niños


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web2.png)



VIctoria Secret:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web3.png)



Y así con todas las demás búsquedas



Dashboard:
Aqui estan todos los productos que tiene el vendedor


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web4.png)



Editar:
Aqui seleccionamos un producto y ponemos editar sus datos, de ejemplo usaremos este:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web5.png)



Aqui vemos los datos del producto:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web6.png)



Y aqui lo vemos modificado:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web7.png)


Y aqui vemos el cambio:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web8.png)

Donde modificamos las unidades disponibles y el precio



Aqui subiremos (crearemos) un producto nuevo, en este caso de niños, dando en el boton de Nuevo producto:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web10.png)



Y nos llevará a este lugar:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web11.png)


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web12.png)



Agregando esta informacion:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web13.png)


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web14.png)



Y podemos ver que aqui se agrego en productos:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web15.png)



Ahora vamos a la pagina principal y vemos esto en la categoria donde lo pusimos, niños:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web16.png)



Eliminar:
Aqui eliminaremos uno de los productos de que estan en la categoria de niños:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web17.png)



Aqui confirmacion la eliminacion:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web18.png)



Y aqui vemos que se elimino:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web19.png)



Y aquí en búsquedas tampoco sale:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web20.png)



Carrito:
Aquí en el carrito de compra podemos ver si tenemos productos o no y ver los precios y el total ya pagar, en este caso no tenemos nada:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web21.png)



Aqui podemos ver nuestro carrito con un solo producto:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web22.png)




Y aquí con dos productos:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web23.png)



Y si modificamos una cantidad de un producto el precio sube, como vemos subi a dos cantidades en el producto de abajo y el precio aumento:


![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/b8a8cae76c159956b1d94d703f1d046d9b4f743f/tianguis/img-admin/web24.png)



# MODELOS (CLAVE DEL PROYECTO)

![EVIDENCIAS](https://github.com/Gutierrez-Jostin/Project_perfum/blob/6e9a50e32b75af3c87b59a38d74f99651c4a2ef4/tianguis/images/Tabla-nm.png)