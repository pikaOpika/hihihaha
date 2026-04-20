from django.urls import path
from catalog.views import index, get_book, search_books


app_name="catalog"

urlpatterns = [
    path('', index, name="index"),
    path('get_book/<int:id>', get_book, name="get_book"),
    path("search_books/", search_books, name="search_books"),  
]

