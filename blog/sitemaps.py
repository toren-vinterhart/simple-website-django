from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)
    
    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item): # We have to use this function for get post url or we can create a get_absolute_url function in post model
        return reverse('blog:single', kwargs={'pid': item.id})