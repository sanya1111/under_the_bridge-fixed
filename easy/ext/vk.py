import requests
import json

def get_label(request):
    if "acc_token" not in request.session:
        raise Exception("havent acc_token")
    data = {
            'access_token' : request.session["acc_token"]
    }
    url = "https://api.vk.com/method/users.get"
    resp = requests.get(url, data)
    str_cont =  resp.content.decode("utf-8") 
    di = json.loads(str_cont)
    if "error" in di:
        raise Exception(di["error_msg"])
    return di["response"][0]
        
def login(request, redirect_page):
    if "code" not in request.GET:
        raise Exception("none code in")
    data = {
            'client_id' : '4985824',
            'client_secret' : 'wrXxFjwL2FglPPazzq0p',
            'code' : request.GET["code"],
            'redirect_uri' : 'http://107.182.225.22/' + redirect_page,
    }
    url = 'https://oauth.vk.com/access_token'
    resp = requests.get(url, data)
    str_cont = resp.content.decode("utf-8") 
    di = json.loads(str_cont)
    if "error" in di:
        raise Exception(di["error_description"])
    request.session["acc_token"] = di["access_token"]
    request.session["id"] = di["user_id"]
    
def exit(request):
    if "acc_token" in request.session:
        del request.session["acc_token"]
    if "id" in request.session:
        del request.session["id"]
    
def is_login(request):
    return "acc_token" in request.session

def get_user_img100(request):
    data = {
        'user_ids' : request.session["id"],
        'fields' : 'photo_100'
    }
    url = "https://api.vk.com/method/users.get"
    resp = requests.get(url, data)
    str_cont =  resp.content.decode("utf-8") 
    di = json.loads(str_cont)
    if "error" in di:
        raise Exception(di["error_msg"])
    cur_user = di["response"][0]
    return cur_user["photo_100"]

    
