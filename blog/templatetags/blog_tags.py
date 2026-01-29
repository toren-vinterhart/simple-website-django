from django import template
from blog.models import Post, Category, Comment

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='sum') # use it in this way in html: {% sum 20 30 %}
def function(a, b):
    return a + b

@register.filter
def snippet(value, arg=100):
    return value[:arg] + "..."

@register.inclusion_tag('test2.html')
def testposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    # categories = Category.objects.all()
    # return {'categories': categories}
    
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()

    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categories': cat_dict}

@register.simple_tag(name='list_count')
def countOfList(list):
    return len(list)

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()



