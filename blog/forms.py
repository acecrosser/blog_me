from django.forms import ModelForm
from django.forms.widgets import Select, Textarea, TextInput, Input
from .models import BlogPost, PostComment, BlogRubric
from captcha.fields import CaptchaField


class PostForm(ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'tags', 'rubric_name',)
        labels = {
            'title': 'Заголовок записи',
            'body': 'Текст записи'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'cols': 80, 'rows': 15, 'class': 'form-control'}),
            'tags': TextInput(attrs={'class': 'form-control'}),
            'rubric_name': Select(attrs={'size': 5, 'class': 'form-control'})
        }


class CommentForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = PostComment
        fields = {'author', 'comment'}
        widgets = {
            'author': Input(attrs={'class': 'form-control'}),
            'comment': Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
        }


class RubricForm(ModelForm):

    class Meta:
        model = BlogRubric
        fields = ('rubric_name', )
        widgets = {
            'rubric_name': TextInput(attrs={'class': 'form-control'})
        }