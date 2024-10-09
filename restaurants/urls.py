from django.urls import path
from . import views

urlpatterns = [
    path('',views.restaurants,name='restaurants'),
    path('<int:restaurants_id>', views.restaurants_listing, name='restaurants_listing'),
  
]