from django.urls import path

import users

import users.views as uv

urlpatterns = [
    path('login', uv.login),
    path('signup', uv.signup),
    path('find_id', uv.find_id, name="find_id"),
    path('find_pw', uv.find_pw),
]