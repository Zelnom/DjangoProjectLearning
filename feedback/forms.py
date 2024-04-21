from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please insert your first "
                                                                                         "name!"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please insert your last name "
                                                                                        "!"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Please enter your email!"}),
            "trainer": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Please write your message!"})
        }


class FeedbackUpdateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please insert your first "
                                                                                         "name!"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Please insert your last name "
                                                                                        "!"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Please enter your email!"}),
            "trainer": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Please write your message!"})
        }