from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('result', views.result, name='result'),
    path('detail', views.detail, name='detail'),
]
