from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "contactus",
                                                        'placeholder': "Ваше имя",
                                                        'type': "type",
                                                        'name': "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "contactus",
                                                        'placeholder': "Ваш email",
                                                        'type': "type",
                                                        'name': "Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "contactus1",
                                                           'placeholder': "Сообщение",
                                                           'type': "type",
                                                           'Message': "Name"}))

    class Meta:
        model = Message
        fields = ('name', 'email', 'message')