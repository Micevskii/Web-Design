from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('pages.urls')),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('apartments/', include('apartments.urls')),
    path('coffee/', include('coffee.urls')),
    path('hotels/', include('hotels.urls')),
    path('buildings/', include('buildings.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('accounts/', include('accounts.urls')),
    path('newsletter/', include('newsletter.urls')), 
    path('i18n/', include('django.conf.urls.i18n')),  # Include this path to enable language switching
    path('contacts/', include('kontakti.urls'))
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

