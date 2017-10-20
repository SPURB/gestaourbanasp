from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail.contrib.modeladmin.options import modeladmin_register
from django_comments.models import Comment


class CommentAdmin(ModelAdmin):
    model = Comment

    menu_label = 'Comentarios'
    menu_icon = 'list-ul'
    menu_order = 200
    add_to_settings_menu = True
    list_display = ('user', 'comment')

modeladmin_register(CommentAdmin)