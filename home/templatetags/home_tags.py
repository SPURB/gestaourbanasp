from django import template
from categories.models import CategoryIndexPage
from categories.models import CategoryStaticPage
from categories.models import Categories

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
	return context['request'].site.root_page


@register.assignment_tag(takes_context=True)
def get_current_page(context):
	# return current page slug.
	return context['request'].get_full_path()


def has_menu_children(page):
	return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because our menu architecture
# requirest that we add a class to the immediate sibling of a dropdown list.
@register.inclusion_tag('home/tags/main_menu.html', takes_context=True)
def main_menu(context, parent, level, calling_page=None):
	menuitems = parent.get_children().live().in_menu()
	for counter, menuitem in enumerate(menuitems):
		# Get tabindex value for proper keyboard navigation.
		menuitem.tabindex = (counter + 1)*(10**level)
		# Get Category color.
		menuitem_category = CategoryIndexPage.objects.get(id=menuitem.id).categoria_id
		menuitem.color = Categories.objects.get(id=menuitem_category).cor
		# Check if page from menu item has subpages.
		menuitem.show_dropdown = has_menu_children(menuitem)
		# Check if page is the active one.
		menuitem.active = (calling_page.path.startswith(menuitem.path)
						   if calling_page else False)
	return {
		'level': level,
		'calling_page': calling_page,
		'menuitems': menuitems,
		'request': context['request'],
	}


# Retrieves the children of the top menu items for the dropdowns.
@register.inclusion_tag('home/tags/main_menu_children.html', takes_context=True)
def main_menu_children(context, parent, parent_tabindex, parent_level, parent_status=False, calling_page=None):
	menuitems_children = parent.get_children()
	menuitems_children = menuitems_children.live().in_menu()
	# The level represents how deep into the menu we are.
	# The main_menu is level 4, which means we can go 3 levels
	# deep into the menu before hitting negative numbers.
	level = parent_level - 1
	for counter, menuitem in enumerate(menuitems_children):
		# Get tabindex value for proper keyboard navigation.
		multiplier = 10**level
		menuitem.tabindex = parent_tabindex + ((counter + 2)*multiplier)
		# Check if page from menu item has subpages.
		menuitem.show_dropdown = has_menu_children(menuitem)
		# Check if page is the active one.
		menuitem.active = (menuitem.slug in calling_page
						   if calling_page else False)

	# The 'Sobre' link will be the first one to get tab index.
	# That's why we start counting at two when assigning tabindex
	# values to the menuitems.
	sobre_tabindex = parent_tabindex + 10**level

	return {
		'level': level,
		'parent': parent,
		'sobre_tabindex': sobre_tabindex,
		'menuitems_children': menuitems_children,
		'request': context['request'],
		'parent_status': parent_status
	}