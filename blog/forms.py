from django import forms
from . import models


class CreateBlogCommentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"type": "text", 'class': "form-control bg-white border-0", 'placeholder': "Your Name", 'style':"height: 55px;"}))
    comment_description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control bg-white border-0", 'rows': "5", 'placeholder': "Comment"}))
    class Meta:
        model = models.BlogComment
        fields = ['title', 'comment_description']
