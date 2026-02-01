from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "/blog/rss/feed/"
    description = 'A blog for traveling'

    def items(self):
        return Post.objects.filter(status=True)
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content[:100]
    
    # No need this method because post model has get_absolute_url method
    # def item_link(self, item):
    #     return reverse('blog:single', args=[item.pk])