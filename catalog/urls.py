from django.urls import path
from catalog.views import (
    index, get_book, search_books, BookDetailView, format_create,
    LiteraryFormatListView, BookListView, AuthorListView,
    AuthorDetailView, LiteraryFormatCreateView, LiteraryFormatUpdateView,
    LiteraryFormatDeleteView
)


app_name="catalog"

urlpatterns = [
    path('', index, name="index"),
    path('literary-formats/', LiteraryFormatListView.as_view(), name="format-list"),
    path('literary-formats/create/', LiteraryFormatCreateView.as_view(), name="format-create"),
    path('literary-formats/<int:pk>/update/', LiteraryFormatUpdateView.as_view(), name="format-update"),
    path('literary-formats/<int:pk>/delete/', LiteraryFormatDeleteView.as_view(), name="format-delete"),
    path('books/', BookListView.as_view(), name="book-list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('authors/', AuthorListView.as_view(), name="author-list"),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('get_book/<int:id>', get_book, name="get_book"),
    path("search_books/", search_books, name="search_books"),  
]

