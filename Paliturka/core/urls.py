from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view()),
    url(r'^new_book$', views.CreateBookView.as_view()),
)