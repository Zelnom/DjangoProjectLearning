from django import forms

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please enter your firs name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please enter your last name"}),
            "course": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please enter your course name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Please enter your email"}),
            "department": forms.Select(attrs={"class": "form-select"}),
        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please enter your firs name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please enter your last name"}),
            "course": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please enter your course name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Please enter your email"}),
            "department": forms.Select(attrs={"class": "form-select"}),
        }


