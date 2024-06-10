from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('music-view/<str:pk>/', views.music_view, name='music-view')
]