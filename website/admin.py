from django.contrib import admin
from website.models import Contact, Newsletter

# Register your models here.


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass
