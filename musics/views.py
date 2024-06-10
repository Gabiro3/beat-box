from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import *
from .forms import *


# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('teacher')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Artist.objects.get(email=name)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, email=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('teacher')
        else:
            messages.error(request, 'Invalid Login credentials')
    context = {'page': page}

    return render(request, 'html/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home') 

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
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
    context = {'beats': beats, 'artists': artists}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def music_view(request, pk):
    music = Music.objects.get(id=pk)
    related_beats = Music.objects.filter(music_type=music.music_type)
    other_music = Music.objects.filter(creator=music.creator)
    context = {'music': music, 'related_beats': related_beats, 'other_music': other_music}
    return render(request, 'music-details.html', context)
