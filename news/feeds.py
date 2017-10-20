from django.contrib.syndication.views import Feed
from django.urls import reverse
from news.models import NewsPage


class LatestNewsFeed(Feed):

	title = "Gestão Urbana SP"
	link = "/noticias/"
	description = "Ultimas noticias no site do Gestao Urbana SP da Secretaria Municipal de Urbanismo e Licenciamento"

	def items(self):
		# Change this later to return only item that we're published this week. Because this will be a weekly feed.
		# Right it returns the last five items without checking.
		return NewsPage.objects.live().order_by('-first_published_at')[:5]

	def item_title(self, item):
		return item.title

	def item_subtitle(self, item):
		return item.subtitulo

