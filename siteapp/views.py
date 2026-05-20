from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404

from .models import Product


def home(request):
    return render(request, 'home.html', {
        'name': 'Your Name',
        'headline': 'Frontend Developer & Designer',
        'intro': 'I build clean, modern websites using Django, HTML, CSS, and JavaScript.',
        'projects': [
            {
                'title': 'Personal Portfolio',
                'description': 'A responsive portfolio website to showcase projects and skills.',
            },
            {
                'title': 'Landing Page',
                'description': 'A simple product landing page with smooth scrolling and animations.',
            },
            {
                'title': 'Blog Template',
                'description': 'A clean blog layout with project details and contact information.',
            },
        ],
        'skills': ['HTML', 'CSS', 'JavaScript', 'Django', 'Responsive Design'],
    })


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})


def _get_cart(request):
    return request.session.get('cart', {})


def cart_view(request):
    cart = _get_cart(request)
    items = []
    total = 0
    for pid_str, qty in cart.items():
        try:
            pid = int(pid_str)
            product = Product.objects.get(pk=pid)
        except (Product.DoesNotExist, ValueError):
            continue
        subtotal = product.price * qty
        total += subtotal
        items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
    return render(request, 'shop/cart.html', {'items': items, 'total': total})


def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    key = str(pk)
    qty = int(request.POST.get('quantity', 1)) if request.method == 'POST' else 1
    cart[key] = cart.get(key, 0) + qty
    request.session['cart'] = cart
    messages.success(request, 'Added to cart.')
    return redirect('cart')


def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    cart.pop(str(pk), None)
    request.session['cart'] = cart
    messages.info(request, 'Removed from cart.')
    return redirect('cart')
