from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
        url(r'^$', TemplateView.as_view(template_name='posts/index.html'), name='index'),
        # url(r'^create$', ),
        # url(r'^view', ),
        ]
