from django.urls import path
from . import views

urlpatterns = [
    path('',views.apartments,name='apartments'),
    path('<int:apartment_id>', views.apartments_listing, name='apartments_listing'),
   
]