from django import template
from sound.models import Genre

register = template.Library()

@register.inclusion_tag('sound/genres.html')
def get_genre_list(cat=None):
    return {
        'genre_list' : Genre.objects.all(),
        'act_cat': cat,
    }