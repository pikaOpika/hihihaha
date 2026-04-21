from django.shortcuts import render
from django.http import HttpResponse, Http404
from catalog.models import Book, Author, LiteraryFormat
from django.views import generic


def index(request):
    books = Book.objects.all()
    context = {
        "num_authors": Author.objects.count(),
        "num_books": Book.objects.count(),
        "num_formats": LiteraryFormat.objects.count(),
        "books": books,
    }
    return render(request, "catalog/index.html", context=context)



class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/format-list.html"
    context_object_name = "formats"

class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book-list.html"
    context_object_name = "books"

class AuthorListView(generic.ListView):
    model = Author
    template_name = "catalog/author-list.html"
    context_object_name = "authors"


def get_book(request, id):
    try:
        return HttpResponse(
            Book.objects.get(pk=id)
        )
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

def search_books(request):
    format_ = request.GET.get("format")
    queryset = Book.objects.all()
    if format_:
        queryset = queryset.filter(format__name=format_)
    return HttpResponse(queryset)

