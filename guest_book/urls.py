from django.urls import path

from guest_book.views import index, add_record, edit_record, delete_record

urlpatterns = [
    path('', index, name='home'),
    path('add/', add_record, name='add_record'),
    path('edit/<int:pk>/', edit_record, name='edit_record'),
    path('delete/<int:pk>/', delete_record, name='delete_record'),
]
