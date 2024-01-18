from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = AuthorForm()
    return render(request, 'booklist/add_author.html', {'form': form})

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = GenreForm()

    return render(request, 'booklist/add_genre.html', {'form': form})
def book_list(request):
    books = Book.objects.all()
    return render(request, 'booklist/book_list.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book.views_count += 1
    book.save()
    return render(request, 'booklist/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = BookForm()
    return render(request, 'booklist/add_book.html', {'form': form})

def update_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = BookForm(instance=book)
    return render(request, 'booklist/update_book.html', {'form': form, 'book': book})
def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'booklist/delete_book.html', {'book': book})