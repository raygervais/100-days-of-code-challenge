from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Hello, World. You\'re at the polls index.')
