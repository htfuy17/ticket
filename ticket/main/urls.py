from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('flower/', views.flower, name='flower'),
    path('booking/', views.booking, name='booking'),
]