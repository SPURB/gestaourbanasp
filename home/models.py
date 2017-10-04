from __future__ import absolute_import, unicode_literals

from modelcluster.fields import ParentalKey

from django import forms
from django.db import models

from colorful.fields import RGBColorField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from news.models import NewsPage
from events.models import Events
from categories.models import Categories


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

		categoria = models.ForeignKey(
			Categories, 
			null=True,
			blank=True,
			on_delete=models.PROTECT,
			default=0
		)

		page = ParentalKey('HomePage', related_name='headlines')

		panels = [
			MultiFieldPanel(
				[
					FieldPanel('titulo'),
					ImageChooserPanel('imagem'),
					FieldPanel('link'),
					FieldPanel('categoria', widget=forms.RadioSelect())
				]
			),
		]

	def get_context(self, request):
		# Update context to include only the last six last published news,
		# ordered by reverse chronological order.
		context = super(HomePage, self).get_context(request)

		newspages = NewsPage.objects.live().order_by('-first_published_at')[:6]
		context['newspages'] = newspages

		# Update context to include only the last three publish events.
		events = Events.objects.all()[:3]
		context['events'] = events

		return context

	content_panels = Page.content_panels + [
		InlinePanel(
			'headlines',
			label="Manchetes",
			help_text="As três primeiras manchetes descritas nesta página serão renderizadas em ordem. Qualquer manchete além da terceira não será renderizada.")
	]


