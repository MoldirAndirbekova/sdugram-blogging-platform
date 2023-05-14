from django.contrib.auth.models import User
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-group px-2 form-control-lg ",
                                             "placeholder": "type something"})
        }
