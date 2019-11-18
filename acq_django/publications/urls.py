from django.urls import path, re_path, include
from .views import PublisherList, PublisherDetail

urlpatterns = [
    re_path(r'^publishers/$', PublisherList.as_view()),
    re_path(r'^publisher_detail/(?P<pk>\d+)/$', PublisherDetail.as_view()),
]
