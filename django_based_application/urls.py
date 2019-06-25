from django.contrib import admin
from django.urls import path, include
from .views import home
from mail.views import (add, MailListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('list/', MailListView.as_view(), name='mail_list'),
]
