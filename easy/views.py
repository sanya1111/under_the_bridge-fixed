from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from .ext.jin2 import JinContext
import os
import json
from .ext import vk 
from django.template.context_processors import request
import http
from django.http.response import Http404

jc = JinContext("easy", "templates")
jc.put_to_globals("static", "/static/easy/")
    
def session_update(request, current_page):
    def refresh():
        jc.put_to_globals("login", None)
        jc.put_to_globals("first_name", None)
        jc.put_to_globals("last_name", None)
        if vk.is_login(request):
            try:
                obj = vk.get_label(request)
                jc.put_to_globals("login", "1")
                jc.put_to_globals("first_name", obj["first_name"])
                jc.put_to_globals("last_name", obj["last_name"])
                print("VK LABEL ", obj)
            except Exception as arg:
                print(arg.args)
                vk.exit(request)             
    def code():    
        try:
            vk.login(request, current_page)
            refresh()
            print("SUCCESS LOGIN TO VK ", request.session["acc_token"], request.session["id"])
        except Exception as arg:
            print(arg.args)
                    
    def exit():
        vk.exit(request)
        refresh()
    
    if "code" in request.GET:
        code()
    if "refresh" in request.GET:
        refresh()
    if "exit" in request.GET:
        exit()
        
def index_page(request):     
    session_update(request, '')
    return HttpResponse(jc.env.get_template('index.html').render())

def self_adverts(request):
    session_update(request, 'self_adverts')
    if not vk.is_login(request):
        return HttpResponseForbidden('<h1>You havent login to see this page</h1>')
    return HttpResponse(jc.env.get_template('self_adverts.html').render())

def self_adverts_ajax(request):
    if not "next" in request.GET:
        return HttpResponseNotFound("bad request")
    next = request.GET["next"]
    id = None
    if vk.is_login(request):
        id = request.session["id"]
    if "id" in request.GET:
        id = request.GET["id"]
    if next == "1":
        return HttpResponse('{"src":"/static/easy/images/test.jpg"}')
    return HttpResponse('{"src":"/static/easy/images/nig.png"}')
