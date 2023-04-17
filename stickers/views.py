from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sticker_select(request):
    return render(request, "stickers/sticker_select.html")
def sticker_select_popup1(request):
    return render(request, "stickers/sticker_select_popup1.html")
def sticker_select_popup2(request):
    return render(request, "stickers/sticker_select_popup2.html")
def sticker_select_popup3(request):
    return render(request, "stickers/sticker_select_popup3.html")
def sticker_select_popup4(request):
    return render(request, "stickers/sticker_select_popup4.html")
def sticker_edit(request):
    return render(request, "stickers/sticker_edit.html")

def sticker_edit_open(request):
    return render(request, "stickers/sticker_edit_open.html")

def sticker_page(request):
    return render(request, "stickers/sticker_page.html")

def sticker_save(request):
    return render(request, "stickers/sticker_save.html")

def sticker_save_open(request):
    return render(request, "stickers/sticker_save_open.html")




