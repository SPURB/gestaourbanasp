# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 15:03
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20170920_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='corpo',
            field=wagtail.wagtailcore.fields.StreamField((('Título', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('Subtítulo', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('Parágrafo', wagtail.wagtailcore.blocks.RichTextBlock()), ('Citação', wagtail.wagtailcore.blocks.BlockQuoteBlock()), ('Imagem', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('Documento', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), ('Página', wagtail.wagtailcore.blocks.PageChooserBlock()), ('HTML', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('Embed', wagtail.wagtailembeds.blocks.EmbedBlock()))),
        ),
    ]
