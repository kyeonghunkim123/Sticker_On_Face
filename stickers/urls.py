from django.urls import path
import stickers.views as stickers

urlpatterns = [
    path('sticker_edit', stickers.sticker_edit, name='sticker_edit'),
    path('sticker_edit_open', stickers.sticker_edit_open, name='sticker_edit_open'),
    path('sticker_page', stickers.sticker_page, name='sticker_page'),
    path('sticker_save', stickers.sticker_save, name='sticker_save'),
    path('sticker_save_open', stickers.sticker_save_open, name='sticker_save_open'),

]
