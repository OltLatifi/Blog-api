# Generated by Django 4.0.5 on 2022-06-19 13:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_image_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
    ]
