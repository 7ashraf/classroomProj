from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('dashboard', views.dashboard),
    path('login', views.loginn),
    path('add_note',views.addNote ),
    path('logout', views.logoutView),
    path('notes/<int:id>', views.getNote),
    path('notes/<int:id>/edit', views.edit)
]