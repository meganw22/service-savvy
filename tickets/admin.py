from django.contrib import admin
from .models import Ticket, Comment, Archive
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Ticket)
class TicketAdmin(SummernoteModelAdmin):
    list_display = ('title', 'job_category', 'priority')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_filter = ('priority',)
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'username', 'body')

# Register your models here.
# admin.site.register(Comment)
admin.site.register(Archive)