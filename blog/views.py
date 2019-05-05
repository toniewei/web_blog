from django.shortcuts import render

# Create your views here.

class home(request):
    context = {}
    render(request,home.html,context)
