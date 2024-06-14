from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('music-view/<str:pk>/', views.music_view, name='music-view'),
    path('artist-view/<str:name>/', views.artist_view, name='artist-view'),
    path('add-artist', views.addArtist, name='add-artist'),
    path('add-music/', views.addMusic, name='add-music'),
    path('delete-music/<str:pk>', views.deleteMusic, name='delete-music'),
    path('add-sample/', views.addSample, name='add-sample'),
    path('add-melody/', views.addMelody, name='add-melody'),
]