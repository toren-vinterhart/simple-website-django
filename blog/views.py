from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post

# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name__iexact=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username__iexact=kwargs['author_username'])

    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number) # notice: get_page automatically handles exceptions and no need to use it in try-except block. if we use .page instead of .get_page it's necessory to use it in try-except block.
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name__iexact=cat_name)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')

# def test(request, pid):
#     post = get_object_or_404(Post, pk=pid)
#     context = {
#         'post': post,
#     }
#     return render(request, 'test.html', context)