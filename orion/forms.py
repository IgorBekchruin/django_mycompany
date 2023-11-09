from django import forms


class MessageForm(forms.Form):
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
        fields = ('name', 'email', 'message')