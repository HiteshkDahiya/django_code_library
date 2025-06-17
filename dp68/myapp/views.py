from django.shortcuts import render
from django.views.generic.base import TemplateView


# class MyTemplateView(TemplateView):
#     template_name = 'myapp/home.html'


class MyTemplateView(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sameer'
        context['roll'] = 101
        print(context)
        print(kwargs)
        return context
