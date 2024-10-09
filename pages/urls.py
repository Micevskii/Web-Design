from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('hotels',views.hotels,name='hotels'),
    path('coffee',views.coffee,name='coffee'),
    path('restaurants',views.restaurants,name='restaurants'),
    path('buildings',views.buildings,name='buildings'),
    path('apartments',views.apartments,name='apartments'),
    path('search', views.search,name='search'),
    path('search2', views.search2,name='search2'),
    path('gallery', views.gallery, name='gallery'),
]
