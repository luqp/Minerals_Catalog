from django.urls import path, re_path

from . import views

app_name = 'minerals'
urlpatterns = [
    path('detail/<int:pk>/', views.mineral_detail, name='detail'),
    path('search/<str:term>/', views.search, name='search'),
    path('search_all/<str:term>/', views.search_in_all, name='search_all'),
    path('', views.index, name='index')
]