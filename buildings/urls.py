from django.urls import path
from . import views

urlpatterns = [
    path('',views.buildings,name='buildings'),
    path('<int:buildings_id>', views.buildings_listing, name='buildings_listing'),
  
]