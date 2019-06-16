from django.urls import path, include
import app_homework_finder.views

urlpatterns = [
    #path('blog/<int:blog_id>',blog.views.detail, name="detail"),
    path('searching/',app_homework_finder.views.searching, name="searching"),
    path('complete',app_homework_finder.views.complete, name="complete"),
]