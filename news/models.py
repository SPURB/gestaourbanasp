#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

from django import forms
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from categories.models import Categories


class NewsIndexPage(Page):

	"""
	News Index Page

	The News Index page will consist of all news stories 
	organized in reverse chronological order.

	"""

	def get_context(self, request):
		# Update context to include only published news,
		# ordered by reverse chronological order.
		context = super(NewsIndexPage, self).get_context(request)
		newspages = self.get_children().live().order_by('-first_published_at')
		context['newspages'] = newspages
		return context


class NewsPage(Page):

	"""
	News Page

	The News page will have the title of the story,
	a subtitle, a featured image, the category of 
	the story and the body of the text.

	""" 

	corpo = StreamField([
		('Parágrafo', blocks.RichTextBlock()),
		('Imagem', ImageChooserBlock()),
		('HTML', blocks.RawHTMLBlock()),
	])

	descricao = models.CharField(
		max_length=500, 
		blank=True,
		help_text="A descrição que vai aparecer na página que lista as notícias."
	)

	subtitulo = models.CharField(
		max_length=250, 
		blank=True,
		help_text="O subtítulo da legenda."
	)

	imagem_principal = models.ForeignKey(
		'wagtailimages.Image', 
		null=True,
		blank=True,
		on_delete=models.SET_NULL, 
		related_name='+',
		help_text="A imagem principal da notícia."
	)

	legenda = models.CharField(
		blank=True, 
		max_length=250,
		help_text="A legenda da imagem principal."
	)

	categoria = models.ForeignKey(
		Categories, 
		null=True,
		blank=True,
		on_delete=models.PROTECT,
		default=0
	)

	date = models.DateField("Data")

	search_fields = Page.search_fields + [
		index.SearchField('subtitulo'),
		index.SearchField('corpo'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('subtitulo', classname="full title"),
		FieldPanel('descricao', classname="full"),
		MultiFieldPanel([
			ImageChooserPanel('imagem_principal'),
			FieldPanel('legenda'),
		], heading="Imagem Principal"),
		StreamFieldPanel('corpo'),
		MultiFieldPanel([
			FieldPanel('date'),
			FieldPanel('categoria', widget=forms.RadioSelect())
		], heading="Marcadores da Notícia")        
	]

	def get_absolute_url(self):
		return 'noticias/%i' % self.id