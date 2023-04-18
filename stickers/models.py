import time
from django.db import models
from stickers.utils import rename_imagefile_to_uuid, date_upload_to


# Create your models here.



class OneImageFile(models.Model):
    name = models.CharField(max_length=10)
    # photo = models.ImageField(upload_to="")
    photo = models.ImageField(null=True, upload_to=date_upload_to, blank=True)




class UploadService(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to=rename_imagefile_to_uuid, blank=True)

    def myImageName(self):
        return self.imgfile.name

    def __str__(self):
        return self.imgfile.name

    # save_dir = models.CharField(max_length=255)
    # myfile = models.FileField(upload_to='') # upload_to='uploads/'



    # def __init__(self, save_dir, myfile):
    #     self.save_dir = save_dir
    #     self.myfile = myfile
    #
    #
    # def save_file(self):
    #     original_file_name = self.myfile
    #     new_file_name = str(int(time.time())) + original_file_name
    #     url = self.save_dir + "/" + new_file_name
    #     print("url : " + url)
    #     self.save()
    #
    #     return new_file_name
