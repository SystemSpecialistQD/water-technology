from tkinter.font import names

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('services/',views.services_page,name='services_page')

   ]
