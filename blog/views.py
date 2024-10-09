from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import location_choices, category_choices

from .models import Blogs

def blog(request):
    blog = Blogs.objects.order_by('-list_date')
    paginator = Paginator(blog,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'blog': paged_listings
    }
    return render(request,'blog_temp/listings.html',context)

def listing(request, blog_id):
    listing = get_object_or_404(Blogs, pk=blog_id)
    blog = Blogs.objects.order_by('-list_date')[:3]
    context = {
        'listing': listing,
        'blog':blog
    }

    return render(request,'blog_temp/listing.html', context)

