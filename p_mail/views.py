from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import MailForm
from urllib.parse import urlencode
from .sendgrid_send_email import send_mail
from .service import add_email_to_emails, get_last_tasks

#создаем представление формы
def get_mail(request):
    # Если форма отправлена через POST запрос
    if request.method == 'POST':
        # представление создаст форму с данными из запроса: “привязать данные к форме”.
        form = MailForm(request.POST)
        # проверка данных формы
        if form.is_valid():
            # действия над данными в form.cleaned_data
            text = form.cleaned_data['text']
            time = form.cleaned_data['time']
            #отправка письма
            #send_mail(text)

            add_email_to_emails(text, time)
            # редерикт на новый адрес
            query_string =  urlencode({'text': text,'time':time})
            return HttpResponseRedirect('/thanks/?{}'.format(query_string))

    # если GET (или любой другой метод) создаем пустой бланк формы
    else:
        form = MailForm()
    #добавление в контекст шаблона для последующего рендеринга
    return render(request, 'mail.html', {'form': form})

    #представление подтверждения отправки
def thanks(request):
    template = loader.get_template('thanks.html')
    data_mail={
        'text': request.GET['text'],
        'time': request.GET['time'],
    }
    return HttpResponse(template.render(data_mail))

def list_tasks(request):
    template = loader.get_template('list_tasks.html')
    data_tasks={
        'tasks': get_last_tasks(),
    }
    return HttpResponse(template.render(data_tasks))


