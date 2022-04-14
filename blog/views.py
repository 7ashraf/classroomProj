from datetime import datetime
from importlib.metadata import requires
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Post


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print(request.user.id)
        return HttpResponseRedirect('dashboard')
    else:
        return HttpResponseRedirect('login')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/blog/dashboard')
        else:
            print('wrong credentials')
            return render(request, 'login.html')
    else :
        print('first time')
    return render(request, 'login.html')
    
def dashboard(request):
   
    if request.method == 'POST':
        postTitle = request.POST['postTitle']
        postContent = request.POST['postContent']
        post = Post()
        post.title = postTitle
        post.author = request.user
        post.content = postContent
        post.date = datetime.today()
        post.save()

    posts = Post.objects.all().filter(
        date__year = datetime.now().year,
        date__month = datetime.now().month,
        date__day = datetime.now().day
    )
    return render(request,'dashboard.html', 
    {
        'posts' : posts
    })

def test(request):
    posts = Post.objects.all()
    return render(request, 'test.html', {
        'posts' : posts
    })

def myPosts(request):
    posts = Post.objects.all()
    return render(request, 'my-posts.html', {
        'posts' : posts
    })