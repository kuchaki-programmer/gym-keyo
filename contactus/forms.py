from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control bg-light border-0 px-4 py-3", 'rows':"4", 'placeholder':"Message"}))
    class Meta:
        model = Message
        fields = ['message']