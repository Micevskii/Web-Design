from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Apartments

def apartments(request):
    apartments = Apartments.objects.order_by('-list_date')
    paginator = Paginator(apartments,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'apartments': paged_listings
    }
    return render(request,'categories/apartments.html',context)

def apartments_listing(request, apartments_id):
    apartments_listing = get_object_or_404(Apartments, pk=apartments_id)
    context = {
        'apartments_listing': apartments_listing
    }

    return render(request,'categories/listing.html', context)
