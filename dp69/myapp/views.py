from django.shortcuts import render
from django.views.generic.base import RedirectView,TemplateView

# Create your views here.
class MyRedirectView(RedirectView):
    url = '/'


class SecondRedirectView(RedirectView):
    pattern_name = "max"
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        print('Hello Whatsup!!')
        # kwargs['id'] = 100
        return super().get_redirect_url(*args,**kwargs)



# permanent = True
# query_string = True