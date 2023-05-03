from django.urls import path
import stickers.views as stickers
from Sticker_On_Face import settings


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('sticker_edit/', stickers.sticker_edit, name='sticker_edit'),
    path('sticker_edit_open', stickers.sticker_edit_open, name='sticker_edit_open'),
    path('sticker_page', stickers.sticker_page, name='sticker_page'),
    path('sticker_save', stickers.sticker_save, name='sticker_save'),
    path('sticker_save_open', stickers.sticker_save_open, name='sticker_save_open'),
    path('sticker_select/', stickers.sticker_select, name='sticker_select'),



# SUBPAGE 추가 2023.04.17 시작
    path('uploadView', stickers.uploadView, name='uploadView'),
    path('upload', stickers.upload, name='upload'),

# SUBPAGE 추가 2023.04.17 끝


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

