from Sticker_On_Face import settings
from django.shortcuts import render

from stickers.models import UploadService


# from django.http import HttpResponse
# Create your views here.


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




# SUBPAGE 추가 2023.04.17 시작


def home(request):
    if request.method == 'POST' and request.FILES:
        myfile = request.FILES['myfile']
    save_dir = settings.MEDIA_ROOT + '/upload/'
    if myfile.name == '':
        return render(request, 'errorView.html')
    upload_service = UploadService()
    file_name = upload_service.save_file(save_dir, myfile)
    context = {'file_name': file_name}

    print("saveDir : " + save_dir)
    print("original_Filename : " + myfile.name)
    print("new_Filename : " + file_name)

    return render(request, 'imageView.html', context)
    return render(request, 'home.html')


def upload(request):
    print("------------1------------")
    if request.method == 'POST' and request.FILES: # POST방식이고 file이 있을때.
        print("------------2------------")
        img = request.FILES['myfile']
        print()
        ######## save_dir = settings.MEDIA_ROOT + '/upload/'
        if img.name == '':
            return render(request, 'stickers/subpage/errorView.html')
        print("------------3------------")

        upload_service = UploadService(title=img.name, imgfile=img)
        print("img.name : ", img.name)
        print("type(img) : ", type(img))
        print("### print(upload_service) : ", print(upload_service))
        print("### print(upload_service) : ", print(upload_service.myImageName()))

        upload_service.save()
        context = {'fileName': img.name}
        print("------------4------------")

        print("original_Filename : " + img.name)
        print("new_Filename : ", 'not yet')
        print("------------5------------")
    else : return render(request, 'stickers/subpage/errorView.html')
    print("------------6------------")

    return render(request, 'stickers/subpage/imageView.html', context)



    #     title = request.POST['title']
    #     content = request.POST['content']
    #     img = request.FILES["imgfile"]
    #     fileupload = FileUpload(
    #         title=title,
    #         content=content,
    #         imgfile=img,
    #     )
    #     fileupload.save()
    #     return redirect('fileupload')
    # else:
    #     fileuploadForm = FileUploadForm
    #     context = {
    #         'fileuploadForm': fileuploadForm,
    #     }
    #     return render(request, 'fileupload.html', context)

def uploadView(request):
    return render(request, "stickers/subpage/uploadView.html")


# SUBPAGE 추가 2023.04.17 끝
