from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
from .data import POSTS, CATEGORIES

def get_published_post_or_404(post_slug):
    post = next((p for p in POSTS if p.get('slug') == post_slug), None)
    if not post or not post.get('is_published'):
        raise Http404("Публикация не найдена")
    return post

def post_list(request):
    search_query = request.GET.get("q", "").strip()
    category_name = request.GET.get("cat", "").strip()

    published_posts = [post for post in POSTS if post.get('is_published')]

    if category_name:
        published_posts = [
            post for post in published_posts
            if post.get('category', {}).get('name') == category_name
        ]

    if search_query:
        published_posts = [
            post for post in published_posts
            if search_query.lower() in post.get('title', '').lower()
        ]

    paginator = Paginator(published_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title': "Лента публикаций",
        'posts': page_obj,
        'page_obj': page_obj,
        'categories': CATEGORIES,
        'q': search_query,
        'cat': category_name,
    }

    if request.htmx:
        return render(request, 'blog/post_list.html#results', context)

    return render(request, 'blog/post_list.html', context)

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, post_slug):
    post = get_published_post_or_404(post_slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_card_fragment(request, post_slug):
    post = get_published_post_or_404(post_slug)
    return render(request, 'blog/post_card_include.html', {'post': post})
