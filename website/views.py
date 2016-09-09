from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'website/Index.html')

def about(request):
    return render(request, 'website/Aboutus.html')
