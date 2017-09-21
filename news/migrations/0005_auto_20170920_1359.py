# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('news', '0004_newstagindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'categoridas de notícias',
            },
        ),
        migrations.AddField(
            model_name='newspage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='news.NewsCategory'),
        ),
    ]
