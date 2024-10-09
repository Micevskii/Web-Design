from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.choices import location_choices, category_choices
from apartments.models import Apartments
from buildings.models import Buildings
from coffee.models import Coffee
from hotels.models import Hotels
from restaurants.models import Restaurants
from blog.models import Blogs
from blog.models import Blogs
from pages.models import Image
from django.http import JsonResponse
from django.views import View


def index(request):
    index = Image.objects.all()
    blog = Blogs.objects.order_by('-list_date')
    context = {
        'index': index,
        'blog': blog,
        'location_choices' : location_choices,
        'category_choices' : category_choices
    }
    return render(request,'pages/index.html',context)


def blog(request):
    return render(request, 'blog_temp/listings.html')

def hotels(request):
    return render(request, 'categories/hotels.html')

def apartments(request):
    return render(request, 'categories/apartments.html')

def buildings(request):
    return render(request, 'categories/buildings.html')

def coffee(request):
    return render(request, 'categories/coffee.html')

def restaurants(request):
    return render(request, 'categories/restaurants.html')

def search(request):
    apartments = Apartments.objects.order_by('-list_date')
    buildings = Buildings.objects.order_by('-list_date')
    coffee = Coffee.objects.order_by('-list_date')
    hotels = Hotels.objects.order_by('-list_date')
    restaurants = Restaurants.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
    
        keywords = request.GET['keywords']
        if keywords:
            apartments = apartments.filter(title__icontains=keywords)
            buildings = buildings.filter(title__icontains=keywords)
            coffee = coffee.filter(title__icontains=keywords)
            hotels = hotels.filter(title__icontains=keywords)
            restaurants = restaurants.filter(title__icontains=keywords)

    # Location
    if 'Локација' in request.GET:
        location = request.GET['Локација']
        if location:
            apartments = apartments.filter(place__icontains=location)
            buildings = buildings.filter(place__icontains=location)
            coffee = coffee.filter(place__icontains=location)
            hotels = hotels.filter(place__icontains=location)
            restaurants = restaurants.filter(place__icontains=location)
    # Categories
    if 'Категории' in request.GET:
        categories = request.GET['Категории']
        if categories:
            apartments = apartments.filter(description__icontains=categories)
            buildings = buildings.filter(description__icontains=categories)
            coffee = coffee.filter(description__icontains=categories)
            hotels = hotels.filter(description__icontains=categories)
            restaurants = restaurants.filter(description__icontains=categories)
    context = {
        'location_choices' : location_choices,
        'category_choices' : category_choices,
        'apartments' : apartments,
        'buildings' : buildings,
        'coffee' : coffee,
        'hotels' : hotels,
        'restaurants' : restaurants,
        'values' : request.GET
    }
    return render(request,'blog_temp/search.html', context)

def search2(request):
    blog = Blogs.objects.order_by('-list_date')
    # Keywords
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            blog = blog.filter(title__icontains=title)
    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page) 

    context = {
        'blog': paged_listings,
        'values': request.GET
    }
    return render(request, 'pages/search2.html', context)

def gallery(request):
    index = Image.objects.all()
    paginator = Paginator(index,9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'index': paged_listings,

    }
    return render(request,'pages/galery.html',context)

