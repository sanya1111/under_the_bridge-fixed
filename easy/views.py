from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from .ext.jin2 import JinContext
import os
import json
from .ext import vk 
from django.template.context_processors import request
import http
from django.http.response import Http404
from .models import Advert, Human
from django.utils import timezone

jc = JinContext("easy", "templates")
EASY_STATIC_PATH = "/static/easy/"
jc.put_to_globals("static", EASY_STATIC_PATH)
    
def get_human_or_create(request, id=None):
    if id == None:
        id = request.session.get("id")
    try:
        return Human.get(id)
    except:
        ret = Human(vk_id=id, name="")
        ret.save()
        return ret

def get_human_adverts(request, id=None):
    return get_human_or_create(request, id).ad_owner.all()

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
            print(request.session["id"])
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
        
def set_refresh(request):
    request.GET = request.GET.copy()
    request.GET["refresh"] = 1 
    
def index_page(request):    
    set_refresh(request)
    session_update(request, '')
    return HttpResponse(jc.env.get_template('index.html').render())

def self_adverts(request):
    set_refresh(request)
    session_update(request, 'self_adverts')
    if not vk.is_login(request):
        return HttpResponseForbidden('<h1>You havent login to see this page</h1>')
#     if "create_empty" in request.GET :
#         human = get_human_or_None(request)
#         if human != None and :
#             Advert.create()
    return HttpResponse(jc.env.get_template('self_adverts.html').render())
    
def search(request):
    set_refresh(request)
    session_update(request, 'self_adverts')
    return HttpResponse(jc.env.get_template('search.html').render())

def self_adverts_ajax(request):
    if "next" in request.GET:
        next = 0
        try :
            next = int(request.GET["next"])
        except:
            pass
        adverts_list = get_human_adverts(request)
        if len(adverts_list) == 0:
            return JsonResponse({"none" : 1})
        if next < 0:
            next = len(adverts_list) - 1
        if next >= len(adverts_list):
            next = 0    
        item =  adverts_list[next] 
        ret = {}
        ret["date"] = item.date
        ret["adress"] = item.adress
        ret["content"] = item.content
        ret["face_img"] = os.path.join(EASY_STATIC_PATH, item.im_content)
        ret["page"] = next
        return JsonResponse(ret)
    if "update" in request.GET:
        if not "advert_id" in request.GET:
            return HttpResponseNotFound("Need advert_id")
        advert_id = 0
        try:
            advert_id = int(request.GET["advert_id"]) 
        except:
            return HttpResponseNotFound("wrong advert_id")
        adverts_list = get_human_adverts(request)
        if advert_id not in range(0, len(adverts_list)):
            return HttpResponseNotFound("wrong advert_id")
        advert = adverts_list[advert_id]
        if "adress" in request.GET:
            advert.adress = request.GET["adress"]         
        if "content" in request.GET:
            advert.content = request.GET["content"] 
        advert.date = timezone.now()
        advert.save()
        return HttpResponse("OK")
    if "create" in request.GET:
        new_ad = Advert(date=timezone.now())
        new_ad.save()
        human = get_human_or_create(request)
        human.ad_owner.add(new_ad)
        return HttpResponse("OK")
    if "remove" in request.GET:
        if not "advert_id" in request.GET:
            return HttpResponseNotFound("Need advert_id")
        advert_id = 0
        try:
            advert_id = int(request.GET["advert_id"]) 
        except:
            return HttpResponseNotFound("wrong advert_id")
        adverts_list = get_human_adverts(request)
        if advert_id not in range(0, len(adverts_list)):
            return HttpResponseNotFound("wrong advert_id")
        adverts_list[advert_id].delete()
        return HttpResponse("OK")


    



    