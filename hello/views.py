from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

print("http://127.0.0.1:8000/hello/VSCode")

# Replace the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    
def test1(request):
    return HttpResponse("Hello World")