from django.urls import path
from . import views
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('<int:pid>', views.blog_single, name='single'),
    path('category/<str:cat_name>', views.blog_view, name='category'),
    path('author/<str:author_username>', views.blog_view, name='author'),
    path('tag/<str:tag_name>', views.blog_view, name='tag'),
    path('search/', views.blog_search, name='search'),
    path('rss/feed/', LatestEntriesFeed()),
    path('test/', views.test, name='test'),
    # path('test/<int:pid>', views.test, name='test'),
]