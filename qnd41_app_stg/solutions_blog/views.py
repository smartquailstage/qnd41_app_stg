from django.shortcuts import render
from wagtail.core.models import Page
from .models import BlogPage_2

def blog_index(request):
    posts = BlogPage_2.objects.live().public().order_by('-date')
    return render(request, 'solutions_blog/blog_page_2.html', {
        'posts': posts,
    })

def blog_post(request, slug):
    post = BlogPage_2.objects.live().public().get(slug=slug)
    return render(request, 'solutions_blog/blog_posted.html', {
        'post': post,
    })