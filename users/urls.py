from django.urls import path

import users

import users.views as uv

urlpatterns = [
    path('login', uv.login, name='login'),
    path('signup', uv.signup, name='signup'),
    path('find_id', uv.find_id, name='find_id'),
    path('find_pw', uv.find_pw, name='find_pw'),
]