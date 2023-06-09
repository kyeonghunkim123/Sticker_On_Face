"""
URL configuration for Sticker_On_Face project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import Sticker_On_Face.views as sv
from users.views import check_Id
from users.views import check_join
from users.views import check_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sv.mainpage),
    path('users/', include('users.urls')),
    path('stickers/', include('stickers.urls')),
    path('check_Id/', check_Id, name='check_Id'),
    path('check_join/', check_join, name='check_join'),
    path('check_login/', check_login, name='check_login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

