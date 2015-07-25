from django.views.generic import TemplateView
from django import http


class YokkoraView(TemplateView):
    template_name = 'hello/yokkora.html'

yokkora = YokkoraView.as_view()
