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