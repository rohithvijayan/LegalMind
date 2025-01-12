from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def ragbot(request):
    return render(request, 'core/ragbot.html')