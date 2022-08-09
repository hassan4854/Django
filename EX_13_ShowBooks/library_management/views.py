from .models import Book
from django.shortcuts import render


def booklist(request):
    book = Book.objects.all()
    context = {'books': book}
    return render(request, template_name='booklist.html', context=context)
