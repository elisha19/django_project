from blog.views import home
from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='blog-name'),
]
