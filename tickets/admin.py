from django.contrib import admin
from .models import Ticket, Comment, Archive
from django_summernote.admin import SummernoteModelAdmin

class TicketAdmin(SummernoteModelAdmin):
    list_display = ('title', 'job_category', 'priority')
    search_fields = ['title']
    list_filter = ('priority',)
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
admin.site.register(Archive)