from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.add_book, name='add'),
    path('list/', views.book_list, name = 'book_list'),
    path('edit/<int:id>/', views.edit_book, name = 'edit'),
    path('delete/<int:id>/' ,views.delete_book, name = 'delete'),
    path('search/', views.search_book, name = 'search'),
]