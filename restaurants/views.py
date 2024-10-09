from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Restaurants

def restaurants(request):
    restaurants = Restaurants.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(restaurants,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'restaurants': paged_listings
    }
    return render(request,'categories/restaurants.html',context)

def restaurants_listing(request, restaurants_id):
    restaurants_listing = get_object_or_404(Restaurants, pk=restaurants_id)
    context = {
        'restaurants_listing': restaurants_listing
    }

    return render(request,'categories/listing.html', context)

