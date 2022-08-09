from django.http import HttpResponse

from .models import Book
from .render import render_to_readable_output


def book_list(request):
    min_price = request.GET.get('min_price') or 0
    max_price = request.GET.get('max_price') or 100000
    author = request.GET.get('author', '')
    name = request.GET.get('name', '')

    all_books = Book.objects.filter(price__gte=min_price,
                                    price__lte=max_price,
                                    author__icontains=author,
                                    name__icontains=name)

    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)
