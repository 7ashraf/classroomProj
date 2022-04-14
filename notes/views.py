from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Notes



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        print(request.user.id)
        return HttpResponseRedirect('dashboard')
    else:
        return HttpResponseRedirect('login')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('dashboard')
        else:
            print('wrong credentials')
            return render(request, 'login.html')
    else :
        print('first time')
    return render(request, 'login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        
        return HttpResponseRedirect('login')
    else:
        notes = Notes.objects.all()
        print(f'{request.user} this is user id {notes[0].id}')
        return render(request, 'dashboard.html', {
            'notes' : notes
        })

def addNote(request):
    if request.method == 'POST':
        note = Notes(noteTitle = request.POST['noteTitle'],
            noteContent = request.POST['noteContent'],
            author = request.user.id)
        note.save()
        return HttpResponseRedirect('dashboard')
    else:
        return render(request, 'add_note.html')

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('home')

def getNote(request, id):
    if request.method == 'POST':
        newNoteContent = request.POST['noteContent']
        print(f'new note content {newNoteContent}')
        note = Notes.objects.get(id = id)
        note.noteContent = newNoteContent
        note.save()
        return render(request, 'note.html', {
        'note' : note
        })
    note = Notes.objects.get(id = id)
    return render(request, 'note.html', {
        'note' : note
    })
def edit(request, id):
    note = Notes.objects.get(id = id)
    return render(request, 'edit.html', {
        'note':note
    })