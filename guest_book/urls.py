from django.urls import path

from guest_book.views import index

urlpatterns = [
    path('', index, name='home'),
]
