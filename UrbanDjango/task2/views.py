from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index1(request):
    return render(request, 'func_template.html')

class index2(TemplateView):
    template_name = 'class_template.html'

