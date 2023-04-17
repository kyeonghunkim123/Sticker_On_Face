from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
import pymysql
import platform


# Create your views here.
def login(request):
    print('1')
    return render(request, "users/login.html")
