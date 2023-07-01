from django.shortcuts import render, get_object_or_404, redirect

from guest_book.forms.guest_book_form import GuestBookForm
from guest_book.forms.search_form import SearchForm
from guest_book.models import GuestBook


def index(request):
    form_search = SearchForm(data=request.GET)
    search = form_search['search'].value()
    records = GuestBook.objects.all().order_by('-create_date').filter(status='active')
    form_record = GuestBookForm()
    if search:
        records = GuestBook.objects.all().order_by('-create_date').filter(status='active', guest_name__icontains=search)
    return render(request, "home.html", {'form_record': form_record, 'form_search': form_search, 'records': records})


def add_record(request):
    form_search = SearchForm(data=request.GET)
    records = GuestBook.objects.all().order_by('-create_date').filter(status='active')
    if request.method == "POST":
        form_record = GuestBookForm(data=request.POST)
        if form_record.is_valid():
            form_record.save()
            return redirect('home')
        else:
            return render(request, 'home.html', {'form_record': form_record, 'form_search': form_search,
                                                 'records': records})
