from django.urls import path

from guest_book.views import index, add_record

urlpatterns = [
    path('', index, name='home'),
    path('add/', add_record, name='add_record'),
]
