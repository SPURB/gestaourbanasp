#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from categories.models import Categories


class Events(Orderable):

		"""
		Events
	
		Each event will have a title, a place, a start date,
		an end date, a start time and an end time.

		The end date will be optional in case the event 
		will happen in a single day.

		"""

		titulo = models.CharField(
			default="Título",
			blank=True, 
			max_length=140, 
			help_text="O título do evento."
		)

		slug = models.CharField(
			default="#",
			blank=True, 
			max_length=140, 
			help_text="A url do evento. Não deve conter nenhum caractere especial."
		)

		categoria = models.ForeignKey(
			Categories, 
			null=True,
			blank=True,
			on_delete=models.PROTECT,
			default=0
		)

		endereco = models.CharField(max_length=255)

		data_inicio = models.DateField("Data de Início")
		data_final = models.DateField("Data Final", blank=True, null=True)

		horario_inicio = models.TimeField("Horário de Início")
		horario_final = models.TimeField("Horário Final")

		page = ParentalKey('EventsIndexPage', related_name='events')

		panels = [
			FieldPanel('titulo'),
			FieldPanel('slug'),
			FieldPanel('endereco'),
			MultiFieldPanel([
				FieldPanel('data_inicio'),
				FieldPanel('data_final')
			], heading='Datas'),
			MultiFieldPanel([
				FieldPanel('horario_inicio'),
				FieldPanel('horario_final')
			], heading='Horários'),
			FieldPanel('categoria', widget=forms.RadioSelect())
		]


class EventsIndexPage(Page):

	"""
	Events Index Page

	The events index page will display all events in the website
	organized in reverse chronological order.

	""" 

	content_panels = Page.content_panels + [
		InlinePanel(
			'events',
			label="Eventos")
	]