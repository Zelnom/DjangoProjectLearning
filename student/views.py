import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent

"""
CreateView -> este o clasa dezvoltata ade Django care va ajuta sa va definiti un obiect in baza date si
afisarea unui formular asociat modelului definit in models.py

Principalele caracteristici:
Formular de creare: automat se genereaza un formular asociat modului pentru a adauga un obiect
Procesarea datelor: gestionarea si procesarea datelor introduse in formular prin validare
Redirectionarea dupa creare: in momentul in care obiectul este creat cu success, utilizatorul
poate fi redirectionat pe pagina dorita de noi
"""


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "student/create_student.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("list-of-students")
    permission_required = "student.add_student"

    def form_valid(self, form):
        student = form.save(commit=False)
        student.save()
        message = (
            f'A fost adaugat un student nou in aplicatie. Informatiile adugate sunt:'
            f'first_name: {student.first_name}, last_name: {student.last_name}, email: {student.email}')
        HistoryStudent.objects.create(message=message, created_at=datetime.datetime.now(),
                                      active=True, user=self.request.user)

        return redirect("list-of-students")


#ListView -> este o clasa dezvoltata de Django care va ajuta pentru afisarea unei lisate de obiecte
# dintr-un model specificat in template (.html)

# Principalele caracteristici:

# Gestionarea listei: automatizeaza procesul de preluare a listei de obiecte dintr-un model

# Template implicit: ListView foloseste un sablon implicit dar va lasa sa folositi si pe al vostru

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "student/list_of_students.html"
    model = Student
    context_object_name: str = "all_students"
    permission_required = "student.view_list_of_students"

    # Metoda get_queryset este un element cheie în clasele de view bazate pe ListView în Django,
    # permițând personalizarea setului de obiecte care sunt recuperate din baza de date și afișate în template.
    # Această metodă oferă flexibilitatea de a filtra, ordona sau limita datele pe care doriți să le prezentați
    # utilizatorilor, în funcție de logica specifică aplicației sau de cerințele de business.

    def get_queryset(self):
        return Student.objects.filter(active=True)

# UpdateView este o clasa generica in Django care simplifica procesul de actualizare a inregistrarilor
# dintr-o baza de date printr-un formular web

# Principalele caracteristici:

# Automatizare: automatizeaza multe din sarcinile asociate cu preluarea unui obiect dintr-o baza de date, afisarea
# unui formular populat cu datele obiectului, validarea datelor trimise prin formular si salvarea acestora.

# Formulare: utilizeaza un formular Django pentru a afisa si valida datele de intrare

# Configurare: permite personalizarea prin atributi, cum ar fi model, form_class, template_name, success_url pentru
# a defini modelul care trebuie actualizat.


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "student/update_student.html"
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy("list-of-students")


# DeleteView este o clasa generica in Django pentru a implementa in interfata stergerea unui obiect

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "student/delete_student.html"
    model = Student
    success_url = reverse_lazy("list-of-students")

# DetailView este o clasa generica in Django pentru a prezenta detalii despre o anumita instanta a unui model.


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = "student/details_student.html"
    model = Student


class HistoryStudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "student/history_student.html"
    model = HistoryStudent
    context_object_name: str = 'history'
    permission_required = "student.view_historystudent"


    def get_queryset(self):
        return HistoryStudent.objects.filter(user=self.request.user)



