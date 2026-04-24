from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from catalog.models import Book, Author, LiteraryFormat
from django.views import generic
from catalog.forms import FormatForm, SearchBook, BookForm
from django.urls import reverse, reverse_lazy


def index(request: HttpRequest):
    request.session["count"] = request.session.get("count", 0) + 1
    context = {
        "num_authors": Author.objects.count(),
        "num_books": Book.objects.count(),
        "num_formats": LiteraryFormat.objects.count(),
        "count": request.session["count"]
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
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchBook(self.request.GET or None) 
        return context
    
    def get_queryset(self):
        form = SearchBook(self.request.GET or None)
        queryset = Book.objects.all()
        if form.is_valid():
            queryset = queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset 
    

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

class BookDetailView(generic.DetailView):
    model = Book

class AuthorDetailView(generic.DetailView):
    model = Author

class LiteraryFormatCreateView(generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:format-list")
    template_name = "catalog/format_form.html"



class LiteraryFormatUpdateView(generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:format-list")
    template_name = "catalog/format_form.html"


class LiteraryFormatDeleteView(generic.DeleteView):
    model = LiteraryFormat
    success_url = reverse_lazy("catalog:format-list")
    template_name = "catalog/confirm_delete_format.html"



def format_create(request: HttpRequest):
    context = {}
    form = FormatForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("catalog:format-list"))
    context["form"] = form
    return render(request, "catalog/format_form.html", context=context)


def book_create(request: HttpRequest):
    context = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("catalog:book-list"))
    context["form"] = form
    return render(request, "catalog/book_form.html", context=context)


