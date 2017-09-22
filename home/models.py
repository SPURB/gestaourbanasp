from __future__ import absolute_import, unicode_literals

from modelcluster.fields import ParentalKey

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):

	"""
	Home Page Template

	The Home page will consist of one to three head stories
	and a the six newest news stories.

	The head stories will display differently depending on
	how many the admin decides to leave there. The minimum
	will be one story and the maximum three stories.

	""" 	

	class Headlines(Orderable):

		titulo = models.CharField(
			default="Título",
			blank=True, 
			max_length=140, 
			help_text="O título da manchete."
		)
		imagem =  models.ForeignKey(
			'wagtailimages.Image', 
			null=True,
			blank=True,
			on_delete=models.SET_NULL, 
			related_name='+',
			help_text="A imagem de fundo da manchete."
		)
		link = models.URLField(
			default="#", 
			blank=True, 
			help_text="O link para onde a manchete irá redirecionar o usuário."
		)

		page = ParentalKey('HomePage', related_name='headlines')

		panels = [
			MultiFieldPanel(
				[
					FieldPanel('titulo'),
					ImageChooserPanel('imagem'),
					FieldPanel('link')
				]
			),
		]

	content_panels = [
		InlinePanel(
			'headlines',
			label="Manchetes",
			help_text="As três primeiras manchetes descritas nesta página serão renderizadas em ordem. Qualquer manchete além da terceira não será renderizada.")
	]

