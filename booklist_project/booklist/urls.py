from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<slug:slug>/', book_detail, name='book_detail'),
    path('add/', add_book, name='add_book'),
    path('book/<slug:slug>/update/', update_book, name='update_book'),
    path('book/<slug:slug>/delete/', delete_book, name='delete_book'),
    path('add_author/', add_author, name='add_author'),
    path('add_genre/', add_genre, name='add_genre')
]