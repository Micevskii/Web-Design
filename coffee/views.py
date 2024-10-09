from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Coffee

def coffee(request):
    coffee = Coffee.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(coffee,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'coffee': paged_listings
    }
    return render(request,'categories/coffee.html',context)

def coffee_listing(request, coffee_id):
    coffee_listing = get_object_or_404(Blogs, pk=coffee_id)
    context = {
        'coffee_listing': coffee_listing
    }

    return render(request,'blog_temp/listing.html', context)
