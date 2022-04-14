import notes
from . import views 
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('login', views.loginView),
    path('dashboard', views.dashboard),
    path('test', views.test),
    path('my-posts', views.myPosts),
    ]