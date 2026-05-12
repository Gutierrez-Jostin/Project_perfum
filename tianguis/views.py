from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ProductForm
from .models import Cart, CartItem

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

# =========================
# 🛒 Ver carrito
# =========================
@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)

    return render(request, 'marketplace/cart_detail.html', {
        'cart': cart
    })


# =========================
# ➕ Agregar producto
# =========================
@login_required
def add_to_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)

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