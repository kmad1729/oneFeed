from django.http import HttpResponse
from django.shortcuts import render
from utils import read_json_to_dict
from models import add_competer_to_file, get_competer_list
import os.path

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

def display_results(request):
    test_path = os.path.join(os.path.dirname(__file__), 'static', 'test.json')
    print test_path
    results = read_json_to_dict(test_path)
    return render(request, 'index.html', dict(results = results))

def added_competer(request):

    return HttpResponse('hello world')

