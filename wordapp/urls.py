from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wordhome/', views.home, name='wordhome'),
    path('result/', views.result, name='result'),
    path('detail/', views.detail, name='detail'),
]
