import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter', 'all')

    if (filter_type == 'all'):
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
    context = {
        'appname' : 'Kicks & Giggles',
        'name': 'Ahmad Wasis Shofiyulloh',
        'class': 'PBP C',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        products_entry = form.save(commit=False)
        products_entry.user = request.user
        products_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

def edit_products(request, id):
    products = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_products.html", context)

def delete_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(products.id),
            'name': products.name,
            'price': products.price,
            'description': products.description,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'products_views': products.products_views,
            'created_at': products.created_at.isoformat() if products.created_at else None,
            'is_featured': products.is_featured,
            'user_id': products.user_id,
        }
        for products in products_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, products_id):
   try:
        products_item = Product.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
        return HttpResponse(status=404)
   
def show_json_by_id(request, products_id):
    try:
        products = Product.objects.select_related('user').get(pk=products_id)
        data = {
            'id': str(products.id),
            'name': products.name,
            'price': products.price,
            'description': products.description,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'products_views': products.products_views,
            'created_at': products.created_at.isoformat() if products.created_at else None,
            'is_featured': products.is_featured,
            'user_id': products.user_id,
            'user_username': products.user.username if products.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_products_entry_ajax(request):
    name = request.POST.get("title")
    price = request.POST.get("price")
    description = request.POST.get("content")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_products = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_products.save()

    return HttpResponse(b"CREATED", status=201)