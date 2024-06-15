from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import *
from .forms import *
from mutagen.mp3 import MP3

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login credentials')
    context = {'page': page}

    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home') 

@login_required(login_url='login')
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    beats = Music.objects.filter(
        Q(title__icontains=q) |
        Q(creator__icontains=q)
    )
    artists = Artist.objects.filter(
        Q(name__icontains=q)
    )
    user = User.objects.filter(id=request.user.id)
    context = {'beats': beats, 'artists': artists, 'user': user}
    return render(request, 'home.html', context)



def music_view(request, pk):
    music = Music.objects.get(id=pk)
    samples = Sample.objects.filter(album=music.title)
    context = {'music': music, 'samples': samples}
    return render(request, 'music-details.html', context)


def artist_view(request, name):
    artist = Artist.objects.get(name=name)
    related_beats = Sample.objects.filter(creator=name)
    other_artists = Artist.objects.filter(genre=artist.genre)
    context = {'artist': artist, 'related_beats': related_beats, 'other_artists': other_artists}
    return render(request, 'artist-details.html', context)


@login_required(login_url='login')
def addArtist(request):
    form = ArtistCreationForm()

    if request.method == 'POST':
        form = ArtistCreationForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.created_by = request.user.name
            artist.save()
            return redirect('home')
        messages.error(request, 'An error occurred during artist creation')
    context = {'form': form}
    return render(request, 'add-artist.html', context)

@login_required(login_url='login')
def addMusic(request):
    form = MusicCreationForm()

    if request.method == 'POST':
        form = MusicCreationForm(request.POST, request.FILES)
        if form.is_valid():
            music_instance = form.save(commit=False)
            music_instance.save()

            # Assuming you have an audio field in your form
            audio_file = music_instance.audio.file.path
            audio = MP3(audio_file)
            duration = audio.info.length  # duration in seconds

            # Create Sample instances with duration
            Sample.objects.create(
                album=music_instance.title,
                creator=music_instance.creator,
                title=music_instance.title,
                duration=duration,
            )
            return redirect('home')
        messages.error(request, 'An error occurred during beat upload')
    context = {'form': form}
    return render(request, 'add-music.html', context)

@login_required(login_url='login')
def deleteMusic(request, pk):
    music = Music.objects.get(id=pk)
    music.delete()
    return redirect('home')

@login_required(login_url='login')
def addSample(request):
    form = SampleCreationForm()
    albums = Music.objects.all()

    if request.method == 'POST':
        form = SampleCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        messages.error(request, 'An error occurred during beats creation')
    context = {'form': form, 'albums':albums}
    return render(request, 'add-sample.html', context)

@login_required(login_url='login')
def addMelody(request):
    form = MelodyCreationForm()

    if request.method == 'POST':
        form = MelodyCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        messages.error(request, 'An error occurred during melody creation')
    context = {'form': form}
    return render(request, 'add-melody.html', context)

