from django.contrib import admin
from django.urls import path, include
import blog.views
import wordapp.views
urlpatterns = [
    path('',blog.views.home, name="home"), # 이것만 blog url 파일로 빼낼 수 없는 이유는?
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')), # http://127.0.0.1:8000/accounts/login/ 이런식으로 들어감
    path('wordapp/', include('wordapp.urls')),
    path('admin/', admin.site.urls),     
]
