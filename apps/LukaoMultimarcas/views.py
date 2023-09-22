from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'LukaoMultimarcas/index.html')

def login(request):
    return render(request, 'LukaoMultimarcas/login.html')