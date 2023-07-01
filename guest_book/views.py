from django.shortcuts import render
from guest_book.forms.search_form import SearchForm
from guest_book.models import GuestBook


def index(request):
    form = SearchForm(data=request.GET)
    search = form['search'].value()
    records = GuestBook.objects.all().order_by('-create_date').filter(status='active')
    if search:
        records = GuestBook.objects.all().order_by('-create_date').filter(status='active', guest_name__icontains=search)
    return render(request, "home.html", {'form': form, 'records': records})
