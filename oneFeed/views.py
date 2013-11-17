from django.http import HttpResponse
from django.shortcuts import render
from models import add_competer_to_file, get_competer_list

def hello(request):
    return HttpResponse("Hello world")


def add_competer(request):
    if 'q' in request.GET:
        c = request.GET['q']
        add_competer_to_file(c)
    else:
        pass
    #return HttpResponse(message)
    competers = get_competer_list()
    return render(request, 'add_competer.html', dict(competers = competers))

def added_competer(request):

    return HttpResponse('hello world')

