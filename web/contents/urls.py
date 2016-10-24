from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from contents.views import (
    ContactView, TextTemplateView, HomeView
)


urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name="index"),

    url(r'^contact/$', ContactView.as_view(
        template_name="contents/contact.html"
    ), name="contact"),

    url(r'^contact/success/$', TemplateView.as_view(
        template_name="contents/contact_success.html"
    ), name="contact_success"),

    # static files
    url(r'^humans.txt$', TextTemplateView.as_view(
        template_name="humans.txt"
    ), name="humans"),

    url(r'^robots.txt$', TextTemplateView.as_view(
        template_name="robots.txt",
    ), name="robots"),

)
