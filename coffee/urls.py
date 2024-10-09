from django.urls import path
from . import views

urlpatterns = [
    path('',views.coffee,name='coffee'),
    path('<int:blog_id>', views.coffee_listing, name='coffee_listing'),
 
]