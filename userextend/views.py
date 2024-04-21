import datetime
import random
import string

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject import settings
from userextend.forms import UserForm
from userextend.models import UserHistory


# Create your views here.

class UserCreateView(CreateView):
    template_name = "userextend/create_user.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("login")

# 'form_valid' este o metoda definita in clase de view si este apelata atunci cand un formular este trimis si validat cu success
    # Atunci utilizatorul completeaza si trimite datele dint-un formular catre serverul pentru validare, programatorul
    # poate sa suplimenteze cu actiuni noi.
    def form_valid(self, form):

        # Customizare first_name si last_name pentru a salva sub forma unui title()

        new_user = form.save(commit=False)
        new_user.first_name = new_user.first_name.title()
        new_user.last_name = new_user.last_name.title()
        #atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user

        # Generarea unui username compus in first_name si last_nma
        # randomdig = ''.join(random.choices(string.digits, k=6))
        # username = new_user.first_name[0] + new_user.last_name + '_' + randomdig
        # new_user.username = username

        new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{random.randint(100000, 999999)}'
        new_user.save()

        # Trimiterea de mail FARA TEMPLATE

        # PASUL 1: In fisierul settings.py din Django Project am configurat serverul de mail: EMAIL_BACKEND, EMAIL_HOST, EMAIL_HOST_USER,
        # EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL, EMAIL_PORT

        # PASUL 2: In aplicatia userextend, in fisierului views.py, in cadrul clasei UserCreateView, in metoda def form_valid()
        # s-a definit variabila subject si variabila message.

        # PASUL 3: S-a utilizat send_mail() pentru a trimite mailuri catre utilizatori

        subject = 'Felicitari! Contul tau a fost creat cu success!'
        message = (
            f'Salut, {new_user.first_name} {new_user.last_name} \n Contul tau a fost creat cu success.\n Pentru autentificare'
            f'acceseaza aplicatia noastra iar nume utilizator pentru autentificare este {new_user.username}')

        # all_students = [ student.email for student in Student.objects.all()]

        # all_students = []
        # for student in Student.objects.all():
        #     all_students.append(student.email)

        # send_mail(subject, message, settings.EMAIL_HOST_USER, [new_user.email])

        # Trimitere de mail CU TEMPLATE

        # PASUL 1: In fisierul settings.py din Django Project am configurat serverul de mail: EMAIL_BACKEND, EMAIL_HOST, EMAIL_HOST_USER,
        # EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL, EMAIL_PORT

        # PASUL 2: In aplicatia userextend, in fisierului views.py, in cadrul clasei UserCreateView, in metoda def form_valid()
        # s-a definit variabila subject si variabila message, dar in cadrul variabilei message s-a folosit get_template pentru a ii atasa
        # un fisier .html din folderul templates numit mail.html.

        # PASUL 3: S-a definit dictionarul stocat in variabila details_user unde alocam elemente ce le dorim accesate in pagina mail.html

        # PASUL 4: Folosind EmailMessage pentru a trimite mailuri catre utilizatori atunci cand acestia isi creeaza un con in aplicatie

        details_user = {
            'fullname': f'{new_user.first_name} {new_user.last_name}',
            'user_name': new_user.username

        }

        subject = 'Felicitari! Contul tau a fost creat cu success!'
        message = get_template('mail.html').render(details_user)

        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [new_user.email])
        mail.content_subtype = 'html'
        # mail.send()

        # Istoric

        message = (
            f'A fost adaugat un user nou in aplicatie la data de {datetime.datetime.now()}. Informatiile adugate sunt:'
            f'first_name: {new_user.first_name}, last_name: {new_user.last_name}, email: {new_user.email}, '
            f'username: {new_user.username}')

        # Adaugarea unei instante noi pentru obiectul UserHistory
        UserHistory.objects.create(history_text=message)

        return redirect('login')