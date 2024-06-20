#from django.http import HttpResponse
from django.shortcuts import render # type: ignore
def homepage(request):
    #return HttpResponse("Hello home page!")
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse("My about page!")
    return render(request, 'aboutpage.html')