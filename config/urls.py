from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),
    path('about/', views.about, name='about'),
    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail')
]
