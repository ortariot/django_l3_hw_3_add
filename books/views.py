from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books_query = Book.objects.all()
    context = {'books': books_query}
    return render(request, template, context)


def books_of_date_view(request, date):
    books_query = Book.objects.order_by('pub_date')
    print(len(books_query))
    paginate = Paginator(books_query, len(books_query.filter(pub_date=date)))

    data_list = paginate.get_page(2)
    books_query = Book.objects.filter(pub_date=date)
    # print(books_query)
    prev_page = data_list.previous_page_number if data_list.has_previous() else None
    next_page = data_list.next_page_number if data_list.has_next() else None


    template = 'books/books_list.html'

    context = {'books': data_list,
               'prev_page_url': prev_page,
               'next_page_url': next_page,
               }
    print(context)
    return render(request, template, context)
