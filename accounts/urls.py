from django.conf.urls import url
from django.urls import path, include
from . import views

# URL Pattern for the account -login-logout-signup
urlpatterns = [
    path('add', views.add, name='add'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
