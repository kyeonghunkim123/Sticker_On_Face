from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
import pymysql
import platform

from mysql.connector import cursor


# Create your views here.
def login(request):
    print('1')
    return render(request, "users/login.html")

def signup(request):
    return render(request, "users/signup.html")

def find_id(request):
    return render(request, "users/find_id.html")

<<<<<<< HEAD
def find_myid(request):
    str_name = request.POST.get("MEMBER_NAME")
    str_tel = request.POST.get("MEMBER_TEL")

    filename="C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps=f.read()
    print(root_ps)
    print(filename)
    dev_ps = root_ps+'dev'

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='STICKER_ON_FACE', charset='utf8')
    cur = conn.cursor()

    sql_select = 'select MEMBER_ID from SOF_MEMBER where MEMBER_NAME = (%s) AND MEMBER_TEL = (%s)'
    val = (str_name, str_tel)
    cursor.execute(sql_select, val)

    row = cur.fetchone()

    if row is None:
        return render(request, "user/find_id.html")
    else:
        str_id = row[0]
        content = f'<h1>{str_id} is your id<h1>'
    return HttpResponse(content)












=======

def find_pw(request):
    return render(request, "users/find_pw.html")
>>>>>>> dev
