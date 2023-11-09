from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render

from mycompany.settings import DEFAULT_FROM_EMAIL
from .forms import MessageForm
from django.views.generic import CreateView
from django.core.mail import send_mail



def contact_view(request):
    if request.method == "GET":
        form = MessageForm()
    elif request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'Сообщение от {name}', message, DEFAULT_FROM_EMAIL, [email])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('contact')
    else:
        return HttpResponse('Неверный запрос.')

    return render(request, 'orion/contact.html', {'form': form})
