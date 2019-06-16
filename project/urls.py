from django.contrib import admin
from django.urls import path, include
import blog.views
import wordapp.views
import portfolio.views
import app_homework_finder.views
from django.conf.urls.static import static #for test media
from django.conf import settings#for test media

urlpatterns = [
    path('',blog.views.home, name="home"), # ast
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')), # http://127.0.0.1:8000/accounts/login/ 이런식으로 들어감
    path('wordapp/', include('wordapp.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('homework_finder/',include('app_homework_finder.urls')),
    path('admin/', admin.site.urls),     
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)