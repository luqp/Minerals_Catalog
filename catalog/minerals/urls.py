from django.urls import path, re_path

from . import views

app_name = 'minerals'
urlpatterns = [
    path('detail/<int:pk>/', views.mineral_detail, name='detail'),
    path('', views.index, name='index')
]