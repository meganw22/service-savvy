from django.contrib import admin
from .models import Ticket, Comment, Archive

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_category', 'priority')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_filter = ('priority',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'username', 'body')

admin.site.register(Archive)