# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 17:43
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170920_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='newspagegalleryimage',
            name='page',
        ),
        migrations.AlterModelOptions(
            name='newscategory',
            options={'verbose_name_plural': 'Categorias de Notícias'},
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='intro',
        ),
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subheading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))),
        ),
        migrations.DeleteModel(
            name='NewsPageGalleryImage',
        ),
    ]