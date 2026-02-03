from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from blog.models import Post, Comment
from blog.forms import CommentModelForm

# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name__iexact=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username__iexact=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

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
    if request.method == 'POST':
        form = CommentModelForm(request.POST, post=pid) # I didn't want to pass pid from hidden input so override __init__ and save methods of CommentModelForm and pass pid here
        if form.is_valid():
            form.save()
            messages.success(request, "You comment has been submited")
        else:
            messages.error(request, "Your comment didn't submited")

    post = get_object_or_404(Post, id=pid, status=1)

    if post.login_require and not request.user.is_authenticated:
        return redirect('accounts:login')
    
    comments = Comment.objects.filter(post=post, approved=True)
    form = CommentModelForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        }
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