from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Buildings

def buildings(request):
    buildings = Buildings.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(buildings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'buildings': paged_listings
    }
    return render(request,'categories/buildings.html',context)

def buildings_listing(request, buildings_id):
    buildings_listing = get_object_or_404(Buildings, pk=buildings_id)
    context = {
        'buildings_listing': buildings_listing
    }

    return render(request,'categories/details.html', context)
