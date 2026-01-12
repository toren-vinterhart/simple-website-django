from django import template
from blog.models import Post

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
