from django.forms import ModelForm
from django.forms.widgets import Select, Textarea
from .models import BlogPost


class PostForm(ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'tags', 'rubric_name',)
        labels = {
            'title': 'Заголовок записи',
            'body': 'Текст записи'
        }
        widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 20}),
            'rubric_name': Select(attrs={'size': 5})
        }
