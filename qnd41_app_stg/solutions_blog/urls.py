from django.urls import path
from . import views

app_name = 'solutions_blog'
urlpatterns = [
    path('post', views.blog_index, name='blog_index'),
    path('<slug:slug>/', views.blog_post, name='blog_post'),
]
