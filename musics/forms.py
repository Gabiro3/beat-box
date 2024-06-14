from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class ArtistCreationForm(ModelForm):

    class Meta:
        model = Artist
        fields = ['name', 'genre', 'cover']

class MusicCreationForm(ModelForm):

    class Meta:
        model = Music
        fields = ['title', 'music_type', 'creator', 'cover']

class SampleCreationForm(ModelForm):

    class Meta:
        model = Sample
        fields = ['title', 'album', 'music_type','creator', 'sample']

class MelodyCreationForm(ModelForm):

    class Meta:
        model = Melody
        fields = ['genre', 'content']