from django.utils.safestring import mark_safe
from django import template
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))
