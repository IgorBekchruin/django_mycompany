from django.shortcuts import redirect, render
from .forms import MessageForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Message
from django.core.mail import send_mail


class ContactView(CreateView):
    form_class = MessageForm
    model = Message
    template_name = 'orion/contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} Почта отправителя: {data["email"]}'
        # email(subject, data['message'])
        return super().form_valid(form)


# # Функция отправки сообщения
# def email(subject, content):
#    send_mail(subject, content, 'отправитель@gmail.com', ['получатель1@gmail.com'])

