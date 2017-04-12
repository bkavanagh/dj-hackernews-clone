from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (
        IndexView, DetailView,
        )


urlpatterns = [
        # url(r'^$', TemplateView.as_view(template_name='posts/index.html'), name='index'),
        url(r'^$', IndexView.as_view(), name='index'),
        url(r'^(?P<id>[0-9]+)/detail/$', DetailView.as_view(), name='detail'),
        # url(r'^create$', ),
        # url(r'^view', ),
        ]
