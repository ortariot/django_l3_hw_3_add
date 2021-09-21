from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_query = Book.objects.all()
    context = {'books' : books_query}
    return render(request, template, context)
