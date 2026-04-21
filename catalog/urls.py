from django.urls import path
from catalog.views import (
    index, get_book, search_books, BookDetailView,
    LiteraryFormatListView, BookListView, AuthorListView
)


app_name="catalog"

urlpatterns = [
    path('', index, name="index"),
    path('literary-formats/', LiteraryFormatListView.as_view(), name="format-list"),
    path('books/', BookListView.as_view(), name="book-list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('authors/', AuthorListView.as_view(), name="author-list"),
    path('get_book/<int:id>', get_book, name="get_book"),
    path("search_books/", search_books, name="search_books"),  
]

