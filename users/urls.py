from django.urls import path

from users.views import check_Id
import users
import users.views as uv

urlpatterns = [
    path('login', uv.login, name='login'),
    path('signup', uv.signup, name='signup'),
    path('find_id', uv.find_id, name='find_id'),
    path('find_pw', uv.find_pw, name='find_pw'),
    path('find_pw_failed', uv.find_pw_failed, name='find_pw_failed'),

    path('check_Id/', check_Id, name='check_Id'),
    path('find_myid/', uv.find_myid, name='find_myid'),
    path('find_mypw/', uv.find_mypw, name='find_mypw')

]

