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
from wagtail.wagtailsnippets.models import register_snippet

from colorful.fields import RGBColorField

import news.models

@register_snippet
class Categories(models.Model):

	"""
	Site Categories Model

	The site will have a wide range of categories.
	Each news, event, headline or page will be bound to one of them.

	The categories will have a slug, a name and a color.

	"""

	nome = models.CharField(max_length=140)
	slug = models.SlugField(unique=True, max_length=80)
	cor = RGBColorField()

	panels = [
		FieldPanel('nome'),
		FieldPanel('slug'),
		FieldPanel('cor')
	]

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'


class CategoryIndexPage(Page):

	"""
	Category Index Page

	Each category will have a home page.

	This page will have the title of the category, a brief description for it,
	the list of live child pages for it and the latest news and events for it.

	"""

	resumo = RichTextField(blank=True, max_length=500)

	imagem_principal = models.ForeignKey(
		'wagtailimages.Image', 
		null=True,
		blank=True,
		on_delete=models.SET_NULL, 
		related_name='+',
		help_text="A imagem principal da noticia."
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

	content_panels = Page.content_panels + [
		FieldPanel('categoria', classname="full"),
		FieldPanel('resumo', classname="full"),
		MultiFieldPanel([
			ImageChooserPanel('imagem_principal'),
			FieldPanel('legenda'),
		], heading="Imagem Principal")
	]

	def get_context(self, request):
		# Update context to include child static pages for the category.
		# Also include the last six news with the given category.
		context = super(CategoryIndexPage, self).get_context(request)

		categorypages = self.get_children().live()
		context['categorypages'] = categorypages

		newspages = news.models.NewsPage.objects.live().filter(categoria_id=self.categoria_id).order_by('-first_published_at')[:6]
		context['newspages'] = newspages
		return context


class CategoryStaticPage(Page):

	"""
	Category Static Page

	Every category can have as many child pages and needed.

	This pages will have any kind of free form content and the 
	only mandatory element for each of them will be the title.

	"""

	descricao = models.CharField(
		max_length=250, 
		blank=True,
		help_text="A descricao que vai aparecer na pasgina index da categoria."
	)

	corpo = StreamField([
		('Paragrafo', blocks.RichTextBlock()),
		('Imagem', ImageChooserBlock()),
		('HTML', blocks.RawHTMLBlock()),
	])

	content_panels = Page.content_panels + [
		FieldPanel('descricao', classname="full"),
		StreamFieldPanel('corpo')
	]


	def get_context(self, request):
		# Add parent Category color to context.
		context = super(CategoryStaticPage, self).get_context(request)

		# Get URL path (ignoring the home path),
		# and get only the first part of the url path,
		# which is the category page path.
		slug = self.get_parent().url_path[6:-1].split('/')[0]
		context['cor'] = CategoryIndexPage.objects.get(slug=slug).categoria.cor
		
		return context