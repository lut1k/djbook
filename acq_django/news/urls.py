from django.urls import re_path, include
from . import views


urlpatterns = [
    re_path(r'^articles/2003/special/$', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='news-year-archive'),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.month_archive,
            name='news-month-archive'),

    re_path(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/', include([
        re_path(r'^history/$', views.history),
        re_path(r'^edit/$', views.edit),
        re_path(r'^discuss/$', views.discuss),
        re_path(r'^permissions/$', views.persmissions),
    ])),

    re_path(r'^persons/$', views.persons, name='news-persons'),
]
