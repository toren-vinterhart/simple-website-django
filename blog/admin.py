from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',)
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    # ordering = ['-created_date']
    search_fields = ['title', 'content']
    list_editable = ['status']
    summernote_fields = ('content',)    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Post, PostAdmin)
