# Generated by Django 4.1.2 on 2022-10-19 21:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="intro",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
