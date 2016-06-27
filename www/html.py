# -*- coding:utf-8 -*-
import urllib  
import urllib2
  
def post(url, data):  
    req = urllib2.Request(url)
    #头信息
    req.add_header('X-CSRF-TOKEN', 'c9e38611-7440-4f97-a008-a77cb19d16e5')

    req.add_header('','')
    req.add_header('','')
    req.add_header('','')
    req.add_header('','')
    req.add_header('','')
    
    data = urllib.urlencode(data)
    response = urllib2.urlopen(req, data)  
    return response.read()