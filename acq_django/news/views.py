from django.shortcuts import render, HttpResponse, redirect
from . import models

# Create your views here.


def special_case_2003(request):
    return HttpResponse("Function 'special_case_2003'")


def year_archive(request, year):
    return render(request, "year_archive.html")


def month_archive(request, year, month):
    return HttpResponse("Function 'month_archive'. \
                        year - {}, month - {}".format(year, month))


def history(request, page_slug, page_id):
    return HttpResponse("Function 'history'")


def edit(request, page_slug, page_id):
    return HttpResponse("Function 'edit'")


def discuss(request, page_slug, page_id):
    return HttpResponse("Function 'discuss'")


def persmissions(request, page_slug, page_id):
    return HttpResponse("Function 'permission")


def persons(request):
    """
    Возвращает всех людей из модели Person.
    """
    person = models.Person.objects.all()
    context = {
        "person": person,
    }
    return render(request, 'persons.html', context)

