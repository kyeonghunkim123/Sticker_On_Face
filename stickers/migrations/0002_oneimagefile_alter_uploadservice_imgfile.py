# Generated by Django 4.2 on 2023-04-18 02:20

from django.db import migrations, models
import stickers.utils


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=stickers.utils.date_upload_to)),
            ],
        ),
        migrations.AlterField(
            model_name='uploadservice',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=stickers.utils.rename_imagefile_to_uuid),
        ),
    ]
