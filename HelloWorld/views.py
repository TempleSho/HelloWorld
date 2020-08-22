from django.http import HttpResponse
from django.views.generic import TemplateView
import os


def helloworldfunction(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(__file__)
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject


class HelloWorldView(TemplateView):
    template_name = 'hello.html'