from django.utils.safestring import mark_safe
from django import template
import datetime as date
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text, extensions=['fenced_code', 'codehilite']))


@register.simple_tag(name='year')
def year():
    return str(date.datetime.now().year)
