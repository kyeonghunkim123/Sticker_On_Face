from django.shortcuts import render
import pymysql
# Create your views here.


def login(request):
    return render(request, "user/login.html")


def join(request):
    return render(request, "user/join_membership.html")

def login_complete(request):
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'


    user_id = request.POST.get('user_id', None)
    user_pw = request.POST.get('user_pw', None)

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    cur = conn.cursor()

    sql_select = 'select usernum, username from userTable where userid = (%s) and password = (%s)'
    val = (user_id, user_pw)
    cur.execute(sql_select, val)

    row = cur.fetchone()

    request.session['user_num'] = row[0]
    request.session['user_name'] = row[1]
    request.session['user_id'] = user_id


    return render(request, "main.html")



def checkTel(data):
    tel = data["tel"]
    result = ""

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    cur = conn.cursor()

    sql_select = 'select usernum from userTable where phonenum = (%s)'
    val = (tel,)
    temp1 = cur.execute(sql_select, val)

    row = cur.fetchone()


    temp = a ? temp1 == None : False
    if (check){
    result = "success";
    } else {
    result = "false";
    }
    return result;

