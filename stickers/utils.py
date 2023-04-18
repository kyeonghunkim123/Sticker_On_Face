import datetime
import os
from uuid import uuid4

def date_upload_to(instance, filename):
    ymd_path = datetime.datetime.now().strftime('%Y/%m/%d')
    upload_to = f'{ymd_path}'
    original_name = filename.split('.')[0]
    ext = filename.split('.')[-1]
    myTimeUUID = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    if instance:
        filename = '{}_{}.{}'.format(original_name , myTimeUUID, ext)
    else:
        filename = '{}.{}'.format(myTimeUUID, ext)

    return os.path.join(upload_to, filename)



def rename_imagefile_to_uuid(instance, filename):
    upload_to = f'media/test/{instance}'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex

    if instance:
        filename = '{}_{}.{}'.format(uuid, instance, ext)
    else:
        filename = '{}.{}'.format(uuid, ext)

    return os.path.join(upload_to, filename)