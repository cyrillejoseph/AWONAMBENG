from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreerUtilisateur
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a ete crée avec succès...')
            return redirect('accesPage')
        else:
            messages.error(request, form.errors)
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def accesPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenue')
            return redirect('accueil')
        else:
            messages.error(request, "Il y a une erreur dans le nom d'utilisateur et/ou du mot de passe")
    return render(request, 'compte/acces.html')


@login_required(login_url='accesPage')
def logoutUser(request):
    logout(request)
    return redirect('accesPage')
