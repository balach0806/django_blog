from django.shortcuts import render
from .data import POSTS

def post_list(request):
    published_posts = [post for post in POSTS if post.get('is_published')]
    context = {
        'page_title': "Лента публикаций",
        'posts': published_posts,
    }
    return render(request, 'blog/post_list.html', context)

def about(request):
    return render(request, 'blog/about.html')