# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 13:50
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorystaticpage',
            name='corpo',
            field=wagtail.wagtailcore.fields.StreamField((('Parágrafo', wagtail.wagtailcore.blocks.RichTextBlock()), ('Imagem', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('Imagem_FULL', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('Documento', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), ('Página', wagtail.wagtailcore.blocks.PageChooserBlock()), ('HTML', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('Embed', wagtail.wagtailembeds.blocks.EmbedBlock()))),
        ),
    ]