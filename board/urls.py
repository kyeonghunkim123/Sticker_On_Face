from django.urls import path

import board.views as board

urlpatterns = [
    path("h_list", board.h_list, name='list'),           # url : localhost:8000/board/h_list
    path("h_register", board.h_register, name="register"),   # url : localhost:8000/board/h_register
]