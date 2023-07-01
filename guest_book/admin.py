from django.contrib import admin

from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'guest_name', 'guest_email', 'status']
    list_filter = ['guest_name', 'status', 'create_date', 'update_date']
    list_display_links = ['id', 'guest_name', 'guest_email', 'status']
    search_fields = ['guest_name', 'guest_email']
    readonly_fields = ['create_date', 'update_date']
    fields = ['guest_name', 'guest_email', 'text_records', 'create_date', 'update_date', 'status']


admin.site.register(GuestBook, GuestBookAdmin)
