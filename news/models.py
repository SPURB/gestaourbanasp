from django import forms
from django.db import models

from modelcluster.fields import ParentalKey 
from modelcluster.fields import ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet


class NewsIndexPage(Page):
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]

	def get_context(self, request):
		# Update context to include only published posts,
		# ordered by reverse chronological order.
		context = super(NewsIndexPage, self).get_context(request)
		newspages = self.get_children().live().order_by('-first_published_at')
		context['newspages'] = newspages
		return context


class NewsPageTag(TaggedItemBase):
	content_object = ParentalKey('NewsPage', related_name='tagged_items')


class NewsTagIndexPage(Page):

	def get_context(self, request):
		# Filter by tag.
		tag = request.GET.get('tag')
		newspages = NewsPage.objects.filter(tags__name=tag)

		# Update template context.
		context = super(NewsTagIndexPage, self).get_context(request)
		context['newspages'] = newspages
		return context


@register_snippet
class NewsCategory(models.Model):
	name = models.CharField(max_length=255)
	icon = models.ForeignKey(
		'wagtailimages.Image', null=True, blank=True,
		on_delete=models.SET_NULL, related_name='+'
	)

	panels = [
		FieldPanel('name'),
		ImageChooserPanel('icon')
	]

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categorias de Notícias'


class NewsPage(Page):
	corpo = StreamField([
		('Título', blocks.CharBlock(classname="full title")),
		('Subtítulo', blocks.CharBlock(classname="full title")),
		('Parágrafo', blocks.RichTextBlock()),
		('Citação', blocks.BlockQuoteBlock()),
		('Imagem', ImageChooserBlock()),
		('Documento', DocumentChooserBlock()),
		('Página', blocks.PageChooserBlock()),
		('HTML', blocks.RawHTMLBlock()),
		('Embed', EmbedBlock()),		
	])
	subtitulo = models.CharField(max_length=250, blank=True)
	categorias = ParentalManyToManyField('news.NewsCategory', blank=True)
	date = models.DateField("Data")
	tags = ClusterTaggableManager(through=NewsPageTag, blank=True)

	search_fields = Page.search_fields + [
		index.SearchField('subtitulo'),
		index.SearchField('corpo'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('subtitulo', classname="full title"),
		StreamFieldPanel('corpo'),
		MultiFieldPanel([
			FieldPanel('date'),
			FieldPanel('tags'),
			FieldPanel('categorias', widget=forms.CheckboxSelectMultiple)
		], heading="Marcadores da Notícia"),
	]
