from django import forms
from . models import TrainerComment

class CreateCommentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control bg-white border-0", 'type': "text", 'style':"height: 55px;", 'placeholder':"Title"}))
    comment_description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control bg-white border-0", 'rows': '5', 'placeholder': "Comment" }))
    class Meta:
        model = TrainerComment
        fields = ['title', 'comment_description']


