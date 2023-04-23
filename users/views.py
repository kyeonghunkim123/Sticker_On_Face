from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
import pymysql
import platform
from django.contrib.auth.models import User




# Create your views here.
def login(request):
    print('1')
    return render(request, "users/login.html")


def signup(request):
    return render(request, "users/signup.html")


def find_id(request):
    return render(request, "users/find_id.html")


def find_pw(request):
    return render(request, "users/find_pw.html")


def check_Id(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)
    print(111111111)

    userid = request.POST.get('userid')
    print(211111111)

    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'


    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='Sticker_On_Face', charset='utf8')

    cur = conn.cursor()

    sql = 'select MEMBER_ID from SOF_MEMBER where MEMBER_ID = (%s) '
    val = (userid)

    cur.execute(sql,val)

    row = cur.fetchone()
    print(row)
    if row:
        count = str(row[0])
    else:
        count = '0'

    exists = count > '0'
    print(exists)
    return JsonResponse({'exists': exists})

def check_join(request):
    print('input')
    if request.method == 'POST':
        username = request.POST.get('username')
        userid = request.POST.get('userid')
        userpw = request.POST.get('userpw')
        userphone = request.POST.get('userphone')
        usermail = request.POST.get('usermail')

        print('input1', username, userid, userpw, userphone, usermail)

        filename = "C:/tilburg_club/tilburg.txt"
        with open(filename) as f:
            root_ps = f.read().strip()
        dev_ps = root_ps + 'dev'
        print('input2')
        conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='Sticker_On_Face', charset='utf8')
        print('input3')
        cur = conn.cursor()
        print('input4')
        sql_insert = 'insert into SOF_MEMBER (MEMBER_NAME, MEMBER_ID, MEMBER_PW, MEMBER_TEL,MEMBER_EMAIL) values(%s,%s,%s,%s,%s)'
        val = (username, userid, userpw, userphone, usermail)
        cur.execute(sql_insert, val)
        print('input5')
        conn.commit()
        print(conn)
        print('input6')
        print('input7')

        conn.close()
        print('input4')

        return JsonResponse({'success': True})


    return JsonResponse({'error': 'Page not found.'}, status=404)


