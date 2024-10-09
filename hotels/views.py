from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Hotels

def hotels(request):
    hotels = Hotels.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(hotels,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'hotels': paged_listings
    }
    return render(request,'categories/hotels.html',context)

def hotels_listing(request, hotels_id):
    hotels_listing = get_object_or_404(Hotels, pk=hotels_id)
    context = {
        'hotels_listing': hotels_listing
    }

    return render(request,'blog_temp/listing.html', context)
