from django.urls import path

from intro import views

urlpatterns = [
    path("list_cars/", views.car, name="list-cars"),
    path("list_of_books/", views.books, name="list-of-books"),
    path("first_page/", views.hello, name="first-page"),
]
