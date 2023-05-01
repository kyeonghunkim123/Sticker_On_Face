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


def find_myid(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        usertel = request.POST.get('usertel')

        print('#####', username, usertel)

        filename = "C:/tilburg_club/tilburg.txt"
        with open(filename) as f:
            root_ps = f.read().strip()
        dev_ps = root_ps + 'dev'
        conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='Sticker_On_Face',
                               charset='utf8')
        cur = conn.cursor()
        sql = 'select MEMBER_ID from SOF_MEMBER where MEMBER_NAME = (%s) and MEMBER_TEL = (%s) '
        val = (username, usertel)
        result =cur.execute(sql, val)
        print(result)

        userid = cur.fetchone()[0] if result == 1 else None
        return JsonResponse({'success': 'True' if userid else 'False', 'userid': userid})

def find_pw(request):
    return render(request, "users/find_pw.html")

def find_pw_failed(request):
    return render(request, "users/find_pw_failed.html")

def find_mypw(request):
    print('##########################')
    if request.method == 'POST':
        userid = request.POST.get('userid')

        print('#####', userid)

        filename = "C:/tilburg_club/tilburg.txt"
        with open(filename) as f:
            root_ps = f.read().strip()
        dev_ps = root_ps + 'dev'
        conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='Sticker_On_Face',
                               charset='utf8')
        cur = conn.cursor()
        sql = 'select MEMBER_PW from SOF_MEMBER where MEMBER_ID = (%s)'
        val = (userid)
        result =cur.execute(sql, val)
        print(result)

    #     if result == 1:
    #         userpassword = cur.fetchone()[0]
    #         return JsonResponse({'success': 'True', 'userpassword': userpassword})
    #     else:
    #         return JsonResponse({'success': 'False'})

    # return JsonResponse({'success': 'False'})

        userpassword = cur.fetchone()[0] if result == 1 else None
        return JsonResponse({'success': 'True' if userpassword else 'False', 'userpassword': userpassword})


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
    cur.execute(sql, val)

    exists = "False" if (cur.fetchone() == None) else "True"
    print("##  print(exists) : ", exists)
    return JsonResponse({'exists': f"{exists}"})


def check_login(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        userpw = request.POST.get('userpw')

        print(111111111)

        filename = "C:/tilburg_club/tilburg.txt"
        with open(filename) as f:
            root_ps = f.read().strip()
        dev_ps = root_ps + 'dev'

        conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='Sticker_On_Face',
                               charset='utf8')

        cur = conn.cursor()

        sql = 'select MEMBER_ID from SOF_MEMBER where MEMBER_ID = (%s) and MEMBER_PW = (%s) '
        val = (userid, userpw)

        result =cur.execute(sql, val)
        print(result)

        exists = "True" if (result == 0) else "False"
        print("##  print(exists) : ", exists)
        return JsonResponse({'success': f"{exists}"})




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

def check_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)
    print(111111111)

    userid = request.POST.get('userid')
    userpw = request.POST.get('userpw')
    print(211111111)

    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'


    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='Sticker_On_Face', charset='utf8')

    cur = conn.cursor()

    sql = 'select MEMBER_ID,MEMBER_PW from SOF_MEMBER where MEMBER_ID = (%s) and MEMBER_PW = (%s) '
    val = (userid,userpw)

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

        result = cur.execute(sql_insert, val)
        exists = "False" if (result == None) else "True"
        print("##  print(exists) : ", exists)

        conn.commit()
        conn.close()
        return JsonResponse({'success': f"{exists}"})

    return JsonResponse({'error': 'Page not found.'}, status=404)

