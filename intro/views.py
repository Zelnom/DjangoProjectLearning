from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hey there August!")


@login_required
def car(request):
    context = {
        "list_of_cars": [
            {
                "name_of_brand": "BMV",
                "color": "red",
                "year": 2018
            },
            {
                "name_of_brand": "Bugatti",
                "color": "purple",
                "age": 2022
            },
            {
                "name_of_brand": "Mercedes",
                "color": "black",
                "year": "2022"
            }
        ]
    }
    return render(request,"intro/list_of_cars.html", context)


@login_required
def books(request):
    info ={
        "list_of_books": [
            {
                "name": "The Law of Human Nature",
                "author": "Robert",
                "purchased": 2022
            },
            {
                "name": "The Power",
                "author": "Rhonda Bryne",
                "purchased": 2020
            },
            {
                "name": "The prince",
                "author": "Niccolo Machiavelli",
                "purchased": 2023
            }
        ]
    }
    return render(request,"intro/list_of_books.html", info)
