from django.urls import path
from exhibition import views


app_name = 'exhibition'
urlpatterns = [
    path('', views.exhibition, name='exhibition'),
    path('exhibitionCreate/', views.exhibitionCreate, name='exhibitionCreate'),
]