from django.shortcuts import render
from .data import POSTS
from django.http import Http404

def post_list(request):
    published_posts = [post for post in POSTS if post.get('is_published')]
    context = {
        'page_title': "Лента публикаций",
        'posts': published_posts,
    }
    return render(request, 'blog/post_list.html', context)

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, post_slug):
    post = next((p for p in POSTS if p['slug'] == post_slug), None)
    
    if not post or not post.get('is_published'):
        raise Http404("Публикация не найдена")
        
    return render(request, 'blog/post_detail.html', {'post': post})
