from django.contrib import admin
from webapp.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'created', 'edited', 'status']
    list_filter = ['name', 'status']
    list_display_links = ['name']
    search_fields = ['name']
    fields = ['name', 'email', 'text', 'created', 'edited', 'status']
    readonly_fields = ['created', 'edited']


admin.site.register(Review, ReviewAdmin)