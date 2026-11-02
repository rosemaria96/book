from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Book
from .forms import BookForm

def home(request):
    return render(request, 'home.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add.html', {'form' : form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})

def edit_book(request, id):
    book = get_object_or_404(Book, book_id = id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance = book)
    return render(request, 'edit.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, book_id = id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete.html', {'book':book})

def search_book(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(book_name__icontains= query) | books.filter(author__icontains = query) | books.filter(category__icontains = query)
    return render(request, 'search.html', {'books':books, 'query':query})

