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
import re

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
    return HttpResponse(jc.env.get_template('self_adverts.html').render())
    
def search(request):
    set_refresh(request)
    session_update(request, 'self_adverts')
    print(request.session["acc_token"])
    return HttpResponse(jc.env.get_template('search.html').render())

def next_ajax(request):
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
    ret["coords"] = (item.coords_x, item.coords_y) 
    ret["content"] = item.content
    ret["face_img"] = os.path.join(EASY_STATIC_PATH, item.im_content)
    ret["page"] = next
    return JsonResponse(ret)

def update_ajax(request):
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
    reg_str = "^([A-Za-zА-Яа-я!?.,;:()0-9\'\"%@-]|\s)+$"
    if "adress" in request.GET and re.match(reg_str, request.GET["adress"]):
        advert.adress = request.GET["adress"]       
    if "coords" in request.GET:
        co = json.loads(request.GET["coords"] )
        advert.coords_x = co[0]
        advert.coords_y = co[1] 
    if "content" in request.GET and re.match(reg_str, request.GET["content"]):
        advert.content = request.GET["content"] 
    advert.date = timezone.now()
    advert.save()
    return HttpResponse("OK")

def create_ajax(request):
    new_ad = Advert(date=timezone.now())
    new_ad.coords_x, new_ad.coords_y = [59.93883244868871,30.308324582031215]
    new_ad.save()
    human = get_human_or_create(request)
    human.ad_owner.add(new_ad)
    return HttpResponse("OK")

def remove_ajax(request):
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

def search_ajax(request):
    if "bounds" not in request.GET:
        return HttpResponseNotFound("FUCK")
    page = 0
    PAGE_LIMIT = 5
    if "page" in request.GET:
        try:
            page = int(request.GET["page"])
        except:
            pass
    bounds = json.loads(request.GET["bounds"])
    filtered = Advert.objects.filter(coords_x__range=(bounds[0], bounds[2]), coords_y__range=(bounds[1], bounds[3]))
    rett = {"next" : (filtered.count() > (page + 1) * PAGE_LIMIT), "prev" : (page > 0)}
    filtered = filtered[page * PAGE_LIMIT : (page + 1) * PAGE_LIMIT]
    ret = []
    for obj in filtered.all():
        ret_obj = {}
        ret_obj["coords"] = (obj.coords_x, obj.coords_y)
        ret_obj["face_img"] = os.path.join(EASY_STATIC_PATH, obj.im_content)
        ret_obj["user_img"] = vk.get_user_img100(request)
        ret_obj["adress"] = obj.adress
        ret_obj["content"] = obj.content
        ret.append(ret_obj)
    rett["response"] = ret
    return JsonResponse(rett)

def ajax(request):
    if "next" in request.GET:
        return next_ajax(request)
    if "update" in request.GET:
        return update_ajax(request)
    if "create" in request.GET:
        return create_ajax(request)
    if "remove" in request.GET:
        return remove_ajax(request)
    if "search" in request.GET:
        return search_ajax(request)
        
            
            


    



    