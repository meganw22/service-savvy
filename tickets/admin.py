from django.contrib import admin
from .models import create_ticket
from django_summernote.admin import SummernoteModelAdmin

class TicketAdmin(SummernoteModelAdmin):
    list_display = ('title', 'job_category', 'priority')
    search_fields = ['title']
    list_filter = ('priority',)
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(create_ticket, TicketAdmin)