from django.http import HttpResponse
from django.shortcuts import render
from utils import read_json_to_dict
from models import add_competer_to_file, get_competer_list
from google_search_results import write_entries_to_json
import os.path

def hello(request):
    return HttpResponse("Hello world")


def add_competer(request):
    print request.GET.keys()
    if 'competer' in request.GET:
        c = request.GET['competer']
        add_competer_to_file(c)
    else:
        print hahhahhah
        pass
    #return HttpResponse(message)
    competers = get_competer_list()
    return render(request, 'index.html')

def display_results(request):
    test_path = os.path.join(os.path.dirname(__file__), 'static', 'my_json.json')
    results = read_json_to_dict(test_path)
    print request.GET.items()
    if 'competitor' in request.GET:
        competitor_list = [i[1] for i in request.GET.items() if 'competitor' in i[0]]
        add_competer_to_file(",".join(competitor_list))
    else:
        print 'hahhahhah'
        pass
    #return HttpResponse(message)
    test_path = os.path.join(os.path.dirname(__file__), 'static', 'my_json.json')

    ###generate json for competitor list
    if competitor_list:
        for c in competitor_list:
            write_entries_to_json(c, test_path)
    
            
    competers = get_competer_list()
    results = read_json_to_dict(test_path)


    return render(request, 'index.html', dict(results = results))

def added_competer(request):

    return HttpResponse('hello world')

