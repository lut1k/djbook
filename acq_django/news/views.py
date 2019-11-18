from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from . import models, forms
from django.views.generic import View

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

# Представления-классы.


def myview(request):
    if request.method == "POST":
        form = forms.MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        else:
            form = forms.MyForm(initial={'key': 'value'})

        return render(request, 'form_template.html', {'form': form})

class MyFormView(View):
    form_class = forms.MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(initial=request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
