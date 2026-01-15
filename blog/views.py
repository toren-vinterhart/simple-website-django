from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name__iexact=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')

# def test(request, pid):
#     post = get_object_or_404(Post, pk=pid)
#     context = {
#         'post': post,
#     }
#     return render(request, 'test.html', context)