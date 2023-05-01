from Sticker_On_Face import settings
from django.shortcuts import render

from stickers.models import UploadService, OneImageFile


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
<<<<<<< HEAD
    return render(request, "stickers/sticker_save_open.html")
=======
    return render(request, "stickers/sticker_save_open.html")



# SUBPAGE 추가 2023.04.17 시작


def home(request):
    print("------------1------------")
    if request.method == 'POST' and request.FILES:  # POST방식이고 file이 있을때.
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
    else:
        return render(request, 'stickers/subpage/errorView.html')
    print("------------6------------")

    return render(request, 'stickers/subpage/imageView.html', context)



def upload(request):
    if request.method == 'POST' and request.FILES: # POST방식이고 file이 있을때.
        photo = request.FILES['myfile']
        if photo.name == '':
            return render(request, 'stickers/subpage/errorView.html')

        oneImageFile = OneImageFile(name=photo.name, photo=photo)
        print(" the name of saved image : ", oneImageFile.photo)
        print(" ### print(oneImageFile.photo) : ", print(oneImageFile.photo))
        print("type(img) : ", type(photo))
        oneImageFile.save()
        context = {
            'fileName' : oneImageFile.name,
            'oneImageFile': oneImageFile}

        print("original_Filename : " + photo.name)
    else : return render(request, 'stickers/subpage/errorView.html')
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
>>>>>>> dev
