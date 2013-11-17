
#import feedparser
import requests
import simplejson

import urllib2
import simplejson


def get_first_2_articles_json(c_name):
    url = ('https://ajax.googleapis.com/ajax/services/feed/find?' +
       'v=1.0&q={}&userip=INSERT-USER-IP'.format(c_name))
    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)
    responseData = simplejson.load(response)['responseData']
    entries = responseData['entries']
    return entries[:2]

def write_entries_to_json(c_name, file_path):
    entries = get_first_2_articles_json(c_name)
    #building the dict
    final_dict = {}
    final_list = []
    for e in entries:
        final_dict['link'] = e['url']
        final_dict['title'] = e['contentSnippet']
        final_list.append(final_dict)
        
    with open(file_path,'w') as f:
        simplejson.dump(final_list, f)
