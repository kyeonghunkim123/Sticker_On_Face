from django.urls import path

import user.views as user

urlpatterns = [
    path("join", user.join),      # url : localhost:8000/user/join
    path("login", user.login),      # url : localhost:8000/user/login
    path("abracadabra", user.login_complete, name="complete_login")
    path("checkTel", user.checkTel, name="checkTel")
]
