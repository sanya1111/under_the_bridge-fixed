from django.conf.urls import url

from . import views

urlpatterns = [
    url("^$", views.index_page),
    url("^self_adverts/", views.self_adverts),
    url("^ajax/", views.ajax),
    url("^search/", views.search),
]