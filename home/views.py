from django.shortcuts import render

def index(request, *args, **kwargs):
    template_name = "index.html"
    return render(request, template_name, {})